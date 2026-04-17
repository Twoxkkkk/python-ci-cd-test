from fastapi import FastAPI
from uvicorn import run

app = FastAPI()


@app.get("/")
def root():
    return "Just rename for test"


if __name__ == "__main__":
    run(app, host="0.0.0.0", port=8000)