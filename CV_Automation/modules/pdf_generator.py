# modules/pdf_generator.py

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import LETTER

def generate_pdf(template_layout, ai_data, output_path):
    c = canvas.Canvas(output_path, pagesize=LETTER)

    for element in template_layout:
        key = element["placeholder"]
        text = ai_data.get(key, "")  # fallback if missing
        x = element["x"]
        y = element["y"]
        font = element["font"]
        size = element["size"]

        c.setFont(font, size)

        # If bullet list, if multiline, etc.
        if element.get("type") == "bullet_list":
            line_spacing = element.get("line_spacing", 15)
            for bullet_item in text:  # text is a list of strings
                c.drawString(x, y, f"- {bullet_item}")
                y -= line_spacing
        elif element.get("type") == "multiline":
            line_spacing = element.get("line_spacing", 15)
            for line in text.split("\n"):
                c.drawString(x, y, line)
                y -= line_spacing
        else:
            # single line
            c.drawString(x, y, text)

    c.save()
    print(f"PDF created at {output_path}")