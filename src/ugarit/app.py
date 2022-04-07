from fastapi import FastAPI

from ugarit.api import api_router

app = FastAPI()

app.include_router(api_router)


@app.get("/")
def get_root() -> str:
    return "Hello, World!"
