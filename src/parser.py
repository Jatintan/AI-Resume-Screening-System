from io import BytesIO
from pathlib import Path
from pypdf import PdfReader
from docx import Document

def extract_text(uploaded_file):
    ext=Path(uploaded_file.name).suffix.lower(); data=uploaded_file.getvalue()
    if ext=='.pdf':
        return '\n'.join(p.extract_text() or '' for p in PdfReader(BytesIO(data)).pages)
    if ext=='.docx':
        return '\n'.join(p.text for p in Document(BytesIO(data)).paragraphs)
    if ext=='.txt': return data.decode('utf-8',errors='ignore')
    raise ValueError('Unsupported file type')
