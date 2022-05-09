import os
import random

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from starlette.responses import FileResponse

from pathlib import Path

from helpers import (
    get_random_integers,
    get_random_alphanumerics,
    get_random_alphabetical_strings,
    get_random_real_numbers
)

app = FastAPI(title="Random Objects")

BASE_PATH = Path(__file__).resolve().parent
TEMPLATES = Jinja2Templates(directory=str(BASE_PATH / "templates"))

OUTPUT_FILE_NAME = "output.txt"
MAXFILESIZE = 2000000  # max file size in bytes

RANDOM_OBJECT_METHODS = {
    "alphabetical": get_random_alphabetical_strings,
    "real": get_random_real_numbers,
    "integers": get_random_integers,
    "alphanumerics": get_random_alphanumerics
}


@app.get("/")
def root(request: Request) -> dict:
    """Renders main page when application starts"""
    return TEMPLATES.TemplateResponse(
        "main.html",
        {"request": request},
    )


@app.get("/generate")
def generate(request: Request) -> dict:
    """Generates output file with random objects and returns download link"""
    generate_random_objects()
    return TEMPLATES.TemplateResponse(
        "main.html",
        {
            "request": request,
            "download_url": f"{request.url_for('root')}download/{OUTPUT_FILE_NAME}"
        },
    )


def generate_random_objects():
    """Generates a output file with random object strings"""
    # clearing output file
    open(OUTPUT_FILE_NAME, 'w').close()
    # setting initial file size to 0
    file_size = 0
    # writing contents to file
    with open(OUTPUT_FILE_NAME, 'a') as f:
        while file_size < MAXFILESIZE:
            random_type = random.choice(list(RANDOM_OBJECT_METHODS.keys()))
            output = RANDOM_OBJECT_METHODS[random_type]
            f.write(output + ', ')
            f.tell()

            # updating current file size
            file_size = os.stat(OUTPUT_FILE_NAME).st_size


@app.get("/download/{item}")
def download_file(request: Request, item: str):
    """Downloads file using requested item in url"""
    return FileResponse(
        f"{BASE_PATH}/{item}",
        media_type='application/octet-stream',
        filename=OUTPUT_FILE_NAME
    )
