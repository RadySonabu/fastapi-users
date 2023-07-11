from fastapi import FastAPI
from mangum import Mangum
from .api.app import api

app = FastAPI()


@app.get("/")
async def index():
    return {"message": "Hello World!"}


app.mount("/api", api)

# For AWS deployment
handler = Mangum(app=app)
