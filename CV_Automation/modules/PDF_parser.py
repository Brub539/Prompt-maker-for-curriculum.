# pdf_parser.py

import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    """
    Extracts and returns all text from a PDF file using PyMuPDF.
    """
    doc = fitz.open(pdf_path)
    extracted_text = []
    for page in doc:
        extracted_text.append(page.get_text())
    doc.close()
    return "\n".join(extracted_text)
