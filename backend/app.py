from fastapi import FastAPI
from fastapi import UploadFile
from fastapi import File

import os

from resume_parser.extract_text import (
    extract_text_from_pdf
)

from resume_parser.parser import (
    parse_resume
)

app = FastAPI()


@app.post("/upload-resume")
async def upload_resume(
    file: UploadFile = File(...)
):

    os.makedirs(
        "uploads",
        exist_ok=True
    )

    file_path = f"uploads/{file.filename}"

    with open(file_path, "wb") as f:
        content = await file.read()
        f.write(content)

    text = extract_text_from_pdf(
        file_path
    )

    profile = parse_resume(
        text
    )

    return profile