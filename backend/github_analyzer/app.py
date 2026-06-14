from fastapi import FastAPI
from fastapi import UploadFile, File

from resume_parser.extract_text import extract_text_from_pdf
from resume_parser.parser import parse_resume

from github_analyzer.github_service import get_github_stats

app = FastAPI()


@app.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):

    # resume logic here

    return {"message": "Resume uploaded"}


@app.get("/github-analysis/{username}")
def github_analysis(username: str):

    return get_github_stats(username)