import uvicorn

if __name__ == "__main__":
    uvicorn.run("app.src.index:app", host="0.0.0.0", log_level="info")
