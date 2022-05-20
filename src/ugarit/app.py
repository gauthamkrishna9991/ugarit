#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
app

This holds the root FastAPI App.
"""

# -- IMPORTS: LIBRARIES

# - Standard Library Imports
# Logging Import
import logging

# - FastAPI Imports
from fastapi import FastAPI

# -- IMPORTS: SELF

# - API Router
from ugarit.api import api_router

# - Server Config
from ugarit.config import ServerConfig


# -- INITIALIZE APP

app = FastAPI(title="Ugarit")

# -- SET CONFIGURATION

config = ServerConfig.cli_parse({"debug": app.debug})

# -- INITIALIZE LOGGER

logging.basicConfig(
    filename=ServerConfig.logfile,
    format="%(levelname)s %(asctime)s %(pathname)s %(message)s",
    datefmt="%Y-%m-%d %I:%M:%S %p",
    encoding="utf-8",
)

# -- Include API Router

app.include_router(api_router)


@app.get("/")
def get_root() -> str:
    """
    get_root

    Get Server Root, Responds with "Hello, World!"
    """
    return "Hello, World!"
