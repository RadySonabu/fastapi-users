import uvicorn

if __name__ == "__main__":
    uvicorn.run("app.index:app", host="0.0.0.0", log_level="info")
