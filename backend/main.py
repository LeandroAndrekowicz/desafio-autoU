import os
from fastapi import FastAPI, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

from backend.use_cases.analize_email_use_case import AnalizeEmail
from backend.utils.preprocess_text import PreprocessText
from backend.utils.read_file_content import ReadFileContent

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_URL = os.getenv("BASE_URL")

app.mount("/static", StaticFiles(directory="frontend"), name="frontend")

@app.get("/")
async def home():
    with open("frontend/index.html", "r", encoding="utf-8") as f:
        html = f.read()
    
    html = html.replace(
        "</head>",
        f"<script>const API_BASE_URL = '{BASE_URL}';</script></head>"
    )
    return HTMLResponse(html)

@app.post("/process")
async def process_email(file: UploadFile = None, text: str = Form(None)):
    content = ""
    if file:
        raw = await file.read()
        content = ReadFileContent.read_file_content(file.filename, raw)
    elif text:
        content = text

    if not content:
        return {"error": "Nenhum conteúdo enviado."}

    clean_text = PreprocessText.preprocess_text(content)
    result = await AnalizeEmail.analyze_email(clean_text)
    return result
