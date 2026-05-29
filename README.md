# 🧠 Resume Matcher with FastAPI

A web-based Resume & Job Description (JD) matching application built using **FastAPI** and **spaCy NLP**. The system extracts skills from resumes and job descriptions, compares them, and generates a matching score based on overlapping skills.

---

## 🚀 Features

* Upload resumes in **PDF, DOCX, TXT, JPG, or PNG** formats
* Extract text using OCR and document parsers
* Perform skill extraction using **spaCy NLP**
* Compare resume skills with job description requirements
* Generate a skill match percentage score
* Simple web interface built with **Jinja2 Templates**

---

## 🛠 Tech Stack

* **Backend:** FastAPI, Python
* **NLP:** spaCy (`en_core_web_sm`)
* **OCR & Parsing:** PyMuPDF, pytesseract, python-docx, Pillow
* **Frontend:** HTML, Jinja2 Templates

---

## 📦 Requirements

* Python 3.8+
* FastAPI
* Uvicorn
* spaCy
* PyMuPDF (`fitz`)
* python-docx
* pytesseract
* Pillow

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/resume-matcher-fastapi.git
cd resume-matcher-fastapi
```

### 2. Create a Virtual Environment (Optional)

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install spaCy Model

```bash
python -m spacy download en_core_web_sm
```

### 5. Run the Application

```bash
uvicorn app:app --reload
```

---

## 🧪 How It Works

1. Upload a resume and enter a job description
2. The application extracts and processes text using NLP techniques
3. Relevant skills are identified from both inputs
4. Matching skills are compared
5. A final skill match score (%) is generated

---

## 📌 Notes

* Placeholder files like `model.pkl`, `vectorizer.pkl`, and `encoder.pkl` can be expanded later for advanced ML-based scoring or classification.
* Make sure **Tesseract OCR** is installed on your system for image-based resume processing.

Install Tesseract OCR:
https://github.com/tesseract-ocr/tesseract

---

## 💡 Future Improvements

* Semantic similarity matching using Sentence Transformers
* AI-powered resume feedback
* Resume ranking system for recruiters
* LLM integration for smarter skill analysis
* Dashboard and analytics support
