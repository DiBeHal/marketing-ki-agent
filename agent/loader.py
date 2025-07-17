# agent/loader.py
import fitz  # PyMuPDF
from bs4 import BeautifulSoup
import requests
from docx import Document

def load_pdf(path):
    doc = fitz.open(path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def load_html(path_or_url):
    if path_or_url.startswith("http"):
        response = requests.get(path_or_url)
        html = response.text
    else:
        with open(path_or_url, "r", encoding="utf-8") as f:
            html = f.read()
    soup = BeautifulSoup(html, "html.parser")
    return soup.get_text(separator="\n")

def load_docx(path):
    doc = Document(path)
    text = "\n".join(para.text for para in doc.paragraphs)
    return text
