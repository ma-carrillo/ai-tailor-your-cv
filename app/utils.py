""" from pdfminer.high_level import extract_text as extract_pdf
from docx import Document

def parse_cv_file(file):
    filename = file.filename.lower()
    if filename.endswith(".pdf"):
        return extract_pdf(file).split("\n")
    elif filename.endswith(".docx"):
        doc = Document(file)
        return [p.text for p in doc.paragraphs if p.text.strip()]
    else:
        return file.read().decode("utf-8").split("\n")

def extract_job_text(text):
    return text.strip().split("\n")
 """