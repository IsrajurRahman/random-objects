import os

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from starlette.responses import FileResponse

from pathlib import Path

app = FastAPI(title="Random Objects")

BASE_PATH = Path(__file__).resolve().parent
TEMPLATES = Jinja2Templates(directory=str(BASE_PATH / "templates"))

RECIPES = {"tea": "milk", "rice": "water"}
OUTPUT_FILE_NAME = "output.txt"
MAXSIZE = 1024

@app.get("/")
def root(request: Request) -> dict:
    return TEMPLATES.TemplateResponse(
        "main.html",
        {"request": request},
    )
    

@app.get("/generate")
def generate(request: Request) -> dict:
    generate_random_objects()
    return TEMPLATES.TemplateResponse(
        "main.html",
        {
            "request": request, 
            "download_url": f"{request.url_for('root')}download/{OUTPUT_FILE_NAME}"
        },
    )

    
def generate_random_objects():
    open (OUTPUT_FILE_NAME, 'w')
    file_size = os.stat(OUTPUT_FILE_NAME).st_size
    print(file_size)
    with open(OUTPUT_FILE_NAME, 'a') as f:                # max file size in bytes
        while file_size >- MAXSIZE:
            f.write('file contents\n')


@app.get("/download/{item}")
def download_file(request: Request, item: str):
    return FileResponse(
        f"{BASE_PATH}/{item}", 
        media_type='application/octet-stream',
        filename=OUTPUT_FILE_NAME
        )

