# This script is to load data from the files in the data folder

from pathlib import Path
from pypdf import PdfReader
from docx import Document

DATA_FOLDER = Path("data/")

def extract_pdf_data(file_path: Path) -> str:
    text = []
    try:
        data = PdfReader(file_path)
        for page in data.pages:
            if page_text := page.extract_text():
                text.append(page_text)
    except Exception as e:
        print(f"Error occurred while reading PDF: {e}")
    return "\n".join(text)

def extract_docx_data(file_path: Path) -> str:
    text = []
    try:
        data = Document(file_path)
        for paragraph in data.paragraphs:
            if paragraph.text:
                text.append(paragraph.text.strip())
    except Exception as e:
        print(f"Error occurred while reading DOCX: {e}")
    return "\n".join(text)

def scan_extract_data() -> list[dict]:
    doc_text = []
    
    if not DATA_FOLDER.exists():
        print(f"{DATA_FOLDER} does not exist.")
        return doc_text
    
    for file_path in DATA_FOLDER.rglob("*"):
        extension = file_path.suffix.lower()
        if not file_path.is_file():
            continue
        
        if extension == ".pdf":
            text = extract_pdf_data(file_path)
            if text.strip():
                doc_text.append({"file_path": str(file_path), "text": text})
        elif extension == ".docx":
            text = extract_docx_data(file_path)
            if text.strip():
                doc_text.append({"file_path": str(file_path), "text": text})

    return doc_text