#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
app

This holds the root FastAPI App.
"""

# -- IMPORTS: LIBRARIES

# - FastAPI Imports
from fastapi import FastAPI

# -- IMPORTS: SELF

# - API Router
from ugarit.api import api_router

# - Server Config
from ugarit.config import ServerConfig


# -- INITIALIZE ROUTER
app = FastAPI()

# -- Include API Router
app.include_router(api_router)

config = ServerConfig.cli_parse({"debug": app.debug})


@app.get("/")
def get_root() -> str:
    """
    get_root

    Get Server Root, Responds with "Hello, World!"
    """
    return "Hello, World!"
