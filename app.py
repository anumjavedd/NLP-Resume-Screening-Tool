from fastapi import FastAPI, Request, Form, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import os
import pickle
import pytesseract
import fitz  # PyMuPDF
from PIL import Image
from io import BytesIO
from docx import Document
import spacy

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Load spaCy NLP model
nlp = spacy.load("en_core_web_sm")

# Load model components (optional if needed for other tasks)
with open("models/model.pkl", "rb") as file:
    model = pickle.load(file)

with open("models/vectorizer.pkl", "rb") as file:
    vectorizer = pickle.load(file)

with open("models/encoder.pkl", "rb") as file:
    encoder = pickle.load(file)

# ---------- File text extraction ----------
def extract_text_from_file(filename: str, file_bytes: bytes) -> str:
    ext = os.path.splitext(filename)[1].lower()

    try:
        if ext == ".pdf":
            text = ""
            with fitz.open(stream=file_bytes, filetype="pdf") as doc:
                for page in doc:
                    text += page.get_text()
            return text

        elif ext == ".docx":
            document = Document(BytesIO(file_bytes))
            return "\n".join([para.text for para in document.paragraphs])

        elif ext == ".txt":
            return file_bytes.decode("utf-8", errors="ignore")

        elif ext in [".jpg", ".jpeg", ".png"]:
            image = Image.open(BytesIO(file_bytes))
            return pytesseract.image_to_string(image)

        else:
            return ""
    except Exception:
        return ""

# ---------- Skill extractor (automatic using spaCy) ----------
def extract_skills(text: str):
    doc = nlp(text)
    candidate_skills = set()

    for chunk in doc.noun_chunks:
        phrase = chunk.text.strip().lower()
        if 1 < len(phrase) < 40 and len(phrase.split()) <= 5:
            candidate_skills.add(phrase)

    for token in doc:
        if token.pos_ in ["PROPN", "NOUN"] and not token.is_stop:
            candidate_skills.add(token.text.lower())

    return list(candidate_skills)

# ---------- Routes ----------
@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/upload", response_class=HTMLResponse)
async def upload_resume(
    request: Request,
    job_desc: str = Form(...),
    resume: UploadFile = File(...)
):
    file_bytes = await resume.read()
    resume_text = extract_text_from_file(resume.filename, file_bytes)

    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_desc)

    matched_skills = list(set(resume_skills) & set(job_skills))
    score = round((len(matched_skills) / len(job_skills)) * 100, 2) if job_skills else 0.0

    result = {
        "score": score,
        "skills": matched_skills
    }

    return templates.TemplateResponse("index.html", {
        "request": request,
        "result": result
    })
