from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

from agents.parser_agent import parse_resume
from agents.analyzer_agent import analyze_resume

import shutil
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.get("/")
def home():
    return {"message": "Resume Analyzer API Running"}

@app.post("/upload")
async def upload_resume(file: UploadFile = File(...)):

    file_path = f"{UPLOAD_FOLDER}/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    resume_text = parse_resume(file_path)

    analysis = analyze_resume(resume_text)

    return analysis