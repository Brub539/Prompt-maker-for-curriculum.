# modules/pdf_extractor.py

import fitz  # PyMuPDF

def extract_layout(pdf_path):
    doc = fitz.open(pdf_path)
    items = []
    for page_index, page in enumerate(doc):
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            block_bbox = block["bbox"]
            for line in block["lines"]:
                for span in line["spans"]:
                    span_data = {
                        "page": page_index,
                        "text": span["text"],
                        "font": span["font"],
                        "size": span["size"],
                        "color": span["color"],
                        "block_bbox": block_bbox,
                        "span_bbox": span["bbox"] if "bbox" in span else None,
                        "origin": span["origin"]
                    }
                    items.append(span_data)
    doc.close()
    return items