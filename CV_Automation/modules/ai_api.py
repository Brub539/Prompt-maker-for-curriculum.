import os
import google.generativeai as genai
import json
import re

def call_gemini_api(prompt, api_key):
    """
    Calls Google's Gemini API.
    """
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')

    generation_config = {
        "temperature": 0.7,
        "top_p": 1,
        "top_k": 32,
        "max_output_tokens": 4096,
    }

    safety_settings = [
        {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
        {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
        {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
        {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    ]

    try:
        response = model.generate_content(
            prompt,
            generation_config=generation_config,
            safety_settings=safety_settings,
            stream=False
        )

        if response and response.text:
            return response.text
        else:
            return "Error: Gemini API returned an empty response."

    except Exception as e:
        return f"Error: Gemini API call failed: {e}"

def call_ai(provider, prompt, api_key):
    """
    Calls the selected AI provider.
    """
    if provider == "Gemini":
        return call_gemini_api(prompt, api_key)
    else:
        raise ValueError(f"Unknown AI provider: {provider}")