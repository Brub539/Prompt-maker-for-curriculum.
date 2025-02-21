import fitz  # PyMuPDF

def extract_pdf_structure(pdf_path):
    doc = fitz.open(pdf_path)
    structure = []
    
    for page in doc:
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            for line in block.get("lines", []):
                for span in line["spans"]:
                    structure.append({
                        "text": span["text"],
                        "font": span["font"],
                        "size": span["size"],
                        "position": span["origin"]
                    })
    
    return structure

# Extract formatting from a sample CV
pdf_file = "BRUNO_MUNIZ_Curriculumm.pdf"  # Ensure the file is in the same folder
format_data = extract_pdf_structure(pdf_file)

# Print extracted data for verification
for entry in format_data[:10]:  # Show first 10 lines
    print(entry)
