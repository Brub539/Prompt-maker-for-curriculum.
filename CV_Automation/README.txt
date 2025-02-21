# AI-Powered CV Generator

This application uses AI to generate CVs (resumes) tailored to specific job postings, leveraging your LinkedIn profile and an existing CV for stylistic and content guidance.

## Prerequisites

*   Python 3.7+
*   A Google Gemini API key (set as an environment variable `GEMINI_API_KEY`).
*   Registered fonts in ReportLab

## Installation

1.  Clone the repository:
    ```bash
    git clone [your_repository_url]
    cd [your_repository_directory]
    ```

2.  Install the required Python packages:
    ```bash
    pip install google-generativeai reportlab Jinja2 fitz PyMuPDF
    ```
    *   **google-generativeai:** For interacting with the Google Gemini API.
    *   **reportlab:** For generating PDFs.
    *   **Jinja2:** For templating the CV content.
    *   **fitz:** For extracting data from PDFs (more powerful alternative to pdfplumber).
    *   **PyMuPDF:** Is needed for fitz
  
3. Register fonts:
    Uncomment the lines with `pdfmetrics.registerFont` and follow the correct path to your ttf files.
    TTF files are needed for the app to run correctly, if they aren't properly setted, the application can run but at the time of generating the PDF file the app is going to crash

## Configuration

1.  Obtain a Google Gemini API key.
2.  Set the API key as an environment variable:
    ```bash
    export GEMINI_API_KEY="YOUR_API_KEY"
    ```
    (Replace `YOUR_API_KEY` with your actual API key).

## Usage

1.  Run the application:
    ```bash
    python gui_app.py
    ```

2.  Follow the on-screen instructions:
    *   Enter the job post information.
    *   Enter your LinkedIn profile summary.
    *   Upload your existing CV as a PDF.
    *   Click "Generate Prompt" to create the prompt for Gemini.
    *   Enter your Gemini API key.
    *   Click "Call AI & Generate CV" to generate the new CV.

3.  The generated CV will be saved in the `generated_cvs` directory.

## Notes

*   The application attempts to replicate the style and structure of the original CV as closely as possible.
*   The accuracy of the style replication depends on the quality of the PDF extraction and the capabilities of the AI model.
*   You may need to adjust the prompt or the PDF extraction code to improve the results.