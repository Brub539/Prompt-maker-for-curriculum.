from flask import Flask, request, send_file
from generate_cv import generate_cv
import os

app = Flask(__name__)

@app.route("/generate_cv", methods=["POST"])
def generate_cv_endpoint():
    data = request.json
    output_path = "generated_cvs/generated_cv.pdf"
    
    generate_cv(data, "templates/cv_template.txt", output_path)
    
    return send_file(output_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
