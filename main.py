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
MAX_FILE_SIZE = 2000000  # max file size in bytes

RANDOM_OBJECT_METHODS = {
    "alphabetical": get_random_alphabetical_strings,
    "real": get_random_real_numbers,
    "integers": get_random_integers,
    "alphanumerics": get_random_alphanumerics
}


@app.get("/")
def root(request: Request) -> TEMPLATES.TemplateResponse:
    """Renders main page when application starts"""
    random_object_counter_dict = {
        "alphabetical": 0,
        "real": 0,
        "integers": 0,
        "alphanumerics": 0
    }
    return TEMPLATES.TemplateResponse(
        "main.html",
        {"request": request, "random_object_counter_dict": random_object_counter_dict},
    )


@app.get("/generate")
def generate(request: Request) -> TEMPLATES.TemplateResponse:
    """Generates output file with random objects and returns download link"""
    random_object_counter_dict = generate_random_objects()
    return TEMPLATES.TemplateResponse(
        "main.html",
        {
            "request": request,
            "download_url": f"{request.url_for('root')}download/{OUTPUT_FILE_NAME}",
            "random_object_counter_dict": random_object_counter_dict
        },
    )


def generate_random_objects() -> dict:
    """Generates a output file with random object strings"""
    # clearing output file
    open(OUTPUT_FILE_NAME, 'w').close()
    # setting initial file size to 0
    file_size = 0
    # initiating random object counter dictionary
    random_object_counter_dict = {
        "alphabetical": 0,
        "real": 0,
        "integers": 0,
        "alphanumerics": 0
    }
    # writing contents to file
    with open(OUTPUT_FILE_NAME, 'a') as f:
        while file_size < MAX_FILE_SIZE:
            random_type = random.choice(list(RANDOM_OBJECT_METHODS.keys()))
            output = RANDOM_OBJECT_METHODS[random_type]()
            f.write(output + ', ')
            f.tell()
            # updating current file size
            file_size = os.stat(OUTPUT_FILE_NAME).st_size
            # updating random object counter
            random_object_counter_dict[random_type] += 1

    return random_object_counter_dict


@app.get("/download/{item}")
def download_file(request: Request, item: str) -> FileResponse:
    """Downloads file using requested item in url"""
    return FileResponse(
        f"{BASE_PATH}/{item}",
        media_type='application/octet-stream',
        filename=OUTPUT_FILE_NAME
    )
