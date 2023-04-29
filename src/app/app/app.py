from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

route = FastAPI()
route.mount("/static", StaticFiles(directory="app/src/app/static"), name="static")
templates = Jinja2Templates(directory="app/src/app/templates")


@route.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse("item.html", {"request": request, "id": id})