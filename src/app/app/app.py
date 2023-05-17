import os

from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

load_dotenv()  # take environment variables from .env.
route = FastAPI()
route.mount("/static", StaticFiles(directory=os.getenv('static_path', 'app/app/static')), name="static")
templates = Jinja2Templates(directory=os.getenv('template_path', 'app/app/template'))


@route.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse("item.html", {"request": request, "id": id})
