# CV_Automation

## Overview

CV_Automation is a set of Python tools designed to simplify and accelerate the creation of tailored CVs (Curriculum Vitae) using AI.  It provides a graphical user interface (GUI) for generating optimized prompts for AI models, extracts layout information from existing PDF CVs to create templates, and populates those templates with AI-generated content to produce customized CVs for different job applications.

## Features

*   **GUI Prompt Generator:** A Tkinter-based GUI for creating effective prompts for AI models like Gemini. This allows you to provide a job description, your LinkedIn summary, and your existing CV content to generate a refined prompt designed to produce new and relevant CV content.
*   **AI API Integration (Gemini):**  Uses the Google Gemini API (via `google.generativeai`) to generate CV content based on the crafted prompts.
*   **PDF Extraction:** Extracts layout information (fonts, sizes, positions) from existing PDF CVs using `PyMuPDF` to understand the structure and create reusable templates.
*   **PDF Generation:**  Generates new CVs in PDF format using `reportlab`, populating the templates with the content produced by the AI.
*   **Templating:** Supports a JSON-based template format to define the structure of the generated PDFs.

## File Structure
CV_Automation/
├── gui_app.py # The main Tkinter GUI application
├── modules/
│ ├── ai_api.py # Module for interacting with AI APIs (Gemini)
│ ├── pdf_generator.py # Module for generating PDFs from templates and data
│ ├── template_builder.py # (Example JSON Template)
│ ├── pdf_extractor.py # Module for extracting layout from existing PDFs
│ └── util.py # (Potentially contains utility functions - not provided in details)
└── README.md # This file


## Dependencies

*   Python 3.6+
*   Tkinter (`tkinter`)
*   PyMuPDF (`fitz`)
*   reportlab (`reportlab`)
*   google-generativeai (`google.generativeai`)

To install dependencies:

```bash
pip install pymupdf reportlab google-generativeai

Setup and Usage
1. Clone the repository:
git clone [repository URL]
cd CV_Automation

Install the dependencies:

pip install pymupdf reportlab google-generativeai
Use code with caution.
Bash
Set up your Gemini API Key:

Obtain an API key from Google Gemini API.

Set the API key as an environment variable

Run the GUI:

python CV_Automation/gui_app.py
Use code with caution.
Bash
Using the GUI:

Paste the Job description on the first Text Area

Paste the LinkedIn summary on the second Text Area

Paste a Base Curriculum on the third Text Area

Click on "Generate Prompt", then copy the text and use it on your AI provider.

Modules Overview
gui_app.py: The main application file. It provides the Tkinter GUI for entering job post information, LinkedIn profile summary, and existing CV text. It generates the prompt to be used with the AI.

modules/ai_api.py: Handles the communication with the AI provider (currently only Gemini). It takes the prompt as input and returns the AI-generated text.

modules/pdf_generator.py: Takes a template (defined in JSON) and the AI-generated content and creates a PDF CV.

modules/pdf_extractor.py: Extracts layout information from existing PDF CVs, allowing you to create templates based on existing designs.

modules/template_builder.py: It shows an example of how to structure the Json template for the PDF generation.

modules/util.py: This file isn't currently provided with details

Example Workflow
Use gui_app.py to generate a prompt based on the Job Description, LinkedIn profile and Base Curriculum.

Use the AI API to generate content from the prompt

Create or use an existing CV template (JSON format) in the modules/template_builder.py style.

Run pdf_generator.py to populate the template with the AI-generated content and create the final PDF CV.

Optionally, use pdf_extractor.py on an existing CV to understand its layout and create a new template.

Contributing
Contributions are welcome! Feel free to submit pull requests with bug fixes, new features, or improvements to the documentation.
