from fastapi import FastAPI
from mangum import Mangum
from app.api.app import api
from app.app.app import route

app = FastAPI()


@app.get("/")
async def index():
    return {"message": "Hello World!"}


app.mount("/api", api)
app.mount("/", route)

# For AWS deployment
handler = Mangum(app=app)
