# generate_cv.py

import json
import os
from reportlab.lib.pagesizes import LETTER
from reportlab.pdfgen import canvas
from jinja2 import Template

def generate_cv_from_json(json_path, template_path, output_path):
    """
    Reads data from a JSON file and generates a CV PDF using ReportLab & Jinja2.
    """
    if not os.path.exists(json_path):
        print(f"Error: JSON file '{json_path}' not found.")
        return
    
    with open(json_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    # Load Jinja2 template
    with open(template_path, "r", encoding="utf-8") as t_file:
        template = Template(t_file.read())

    filled_text = template.render(data)

    # Create a PDF
    pdf = canvas.Canvas(output_path, pagesize=LETTER)
    pdf.setFont("Helvetica", 12)
    y_position = 750  # Start near top

    # Simple line-by-line writing
    for line in filled_text.split("\n"):
        pdf.drawString(50, y_position, line)
        y_position -= 20

    pdf.save()
    print(f"CV successfully generated: {output_path}")