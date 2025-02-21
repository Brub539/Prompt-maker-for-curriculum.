import sys
import os
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext, ttk

###########################################
#  Prompt Generation ONLY
###########################################
def create_content_prompt(job_post, linkedin_data, curriculum_text):
    """Creates the prompt for the first API call (content generation)."""

    prompt = f"""You are an expert in writing compelling CV content.

I will provide:

1. A job post.
2. My LinkedIn profile summary.
3. My existing CV text content.

Your ONLY goal is to: Create *new* content for my CV, focusing on the job post and highlighting relevant skills and experience from my LinkedIn and existing CV. Write this resume as a human, not an AI.
*YOU MUST NOT WRITE AS A AI (Don't use ANY AI writing traits), the writing must be seen as human like. with human traits.*

Here is the information:

Job Post:
{job_post}

LinkedIn Profile Summary:
{linkedin_data}

Curriculum Text:
{curriculum_text}

Output: The complete text content for my new CV.
"""
    return prompt

###########################################
#  The main Tkinter GUI (Prompt Only)
###########################################

root = tk.Tk()
root.title("CV Content Prompt Generator")
root.geometry("800x600")

# -- Step 1: Data Entry (Job, LinkedIn, Curriculum)
job_post_var = ""
linkedin_var = ""
curriculum_var = ""

job_text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=8)
linkedin_text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=6)
curriculum_text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=6)

def load_job_text():
    global job_post_var
    job_post_var = job_text_area.get("1.0", tk.END).strip()
    messagebox.showinfo("Loaded", "Job post loaded into memory")

def load_linkedin_text():
    global linkedin_var
    linkedin_var = linkedin_text_area.get("1.0", tk.END).strip()
    messagebox.showinfo("Loaded", "LinkedIn data loaded into memory")

def load_curriculum_text():
    global curriculum_var
    curriculum_var = curriculum_text_area.get("1.0", tk.END).strip()
    messagebox.showinfo("Base Curriculum text loaded into memory")

# Step 2: Generate Prompt
prompt_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=12)

def generate_prompt():
    global job_post_var, linkedin_var, curriculum_var
    if not job_post_var:
        messagebox.showerror("Error", "No job info loaded")
        return
    if not linkedin_var:
        messagebox.showerror("Error", "No LinkedIn info loaded")
        return
    if not curriculum_var:
        messagebox.showerror("Error", "No curriculum info loaded")
        return

    # Create content prompt
    content_prompt = create_content_prompt(job_post_var, linkedin_var, curriculum_var)

    prompt_area.config(state=tk.NORMAL)
    prompt_area.delete("1.0", tk.END)
    prompt_area.insert(tk.END, content_prompt)
    prompt_area.config(state=tk.DISABLED)
    messagebox.showinfo("Prompt Generated", "Prompt is ready for review. Copy and paste it into your AI tool.")

##################################
# UI LAYOUT
##################################
tk.Label(root, text="JOB POST INFO: Paste & then 'Load'").pack(pady=2)
job_text_area.pack(pady=2)
tk.Button(root, text="Load Job Info", command=load_job_text).pack(pady=2)

tk.Label(root, text="LINKEDIN INFO: Paste & then 'Load'").pack(pady=2)
linkedin_text_area.pack(pady=2)
tk.Button(root, text="Load LinkedIn Info", command=load_linkedin_text).pack(pady=2)

tk.Label(root, text="BASE CURRICULUM: Paste & then 'Load'").pack(pady=2)
curriculum_text_area.pack(pady=2)
tk.Button(root, text="Load Curriculum", command=load_curriculum_text).pack(pady=2)

tk.Button(root, text="Generate Prompt", command=generate_prompt, bg="green", fg="white").pack(pady=5)

tk.Label(root, text="PROMPT REVIEW").pack(pady=2)
prompt_area.pack(pady=2)

root.mainloop()