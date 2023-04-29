from fastapi import FastAPI
from mangum import Mangum
from .api.app import api
from .app.app import route

app = FastAPI()

app.mount("/api", api)
app.mount("", route)


@app.get("")
async def authenticated_route():
    return {"message": "Hello World!"}


# For AWS deployment
handler = Mangum(app=app)
