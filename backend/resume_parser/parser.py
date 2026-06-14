import os
import json

import google.generativeai as genai

from dotenv import load_dotenv

from .utils import clean_json_response

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.0-flash"
)


def parse_resume(resume_text: str):

    prompt = f"""
You are an expert resume parser.

Extract information from the resume.

Return ONLY valid JSON.

Schema:

{{
    "name":"",
    "email":"",
    "phone":"",
    "skills":[],
    "education":[],
    "experience":[],
    "projects":[
        {{
            "title":"",
            "description":"",
            "tech_stack":[]
        }}
    ]
}}

Resume:

{resume_text}
"""

    response = model.generate_content(prompt)

    cleaned = clean_json_response(
        response.text
    )

    return json.loads(cleaned)