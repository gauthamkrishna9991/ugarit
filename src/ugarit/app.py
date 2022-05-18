from fastapi import FastAPI

from ugarit.api import api_router
from ugarit.config import ServerConfig

app = FastAPI()

app.include_router(api_router)

config = ServerConfig.cli_parse({"debug": app.debug})


@app.get("/")
def get_root() -> str:
    return "Hello, World!"
