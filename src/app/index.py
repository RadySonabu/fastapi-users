from fastapi import FastAPI, Request
from mangum import Mangum
from fastapi.responses import HTMLResponse
from .app.app import templates
# from .api.app import api
# from .app.app import route

app = FastAPI()


@app.get("/")
async def index():
    return {"message": "Hello World!"}


@app.get("/sample/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse("item.html", {"request": request, "id": id})

# app.mount("/api", api)
# app.mount("/ui", route)

# For AWS deployment
handler = Mangum(app=app)
