#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
`api/base`

Base Application

This holds the base imports for API to be shared among all files.
"""


import logging
from sqlalchemy.orm import Session

from ugarit import schemas
from ugarit.config import ServerConfig
from ugarit.database import SessionLocal, engine

logging.basicConfig(
    filename=ServerConfig.logfile,
    format="%(asctime)s %(pathname)s %(message)s",
    datefmt="%Y-%m-%d %I:%M:%S %p",
    encoding="utf-8",
)

logger = logging.getLogger()

logger.setLevel(logging.INFO)

if ServerConfig.debug:
    logger.info(msg="Database in Debug Mode", exc_info=True)
    schemas.base.Base.metadata.drop_all(bind=engine)
    logger.info("ugarit/api/base: All Tables Dropped")
    schemas.base.Base.metadata.create_all(bind=engine)
    logger.info("ugarit/api/base: All Tables Created")


# Dependency
def get_db() -> Session:
    """
    Get a Session Object
    """
    db_session = SessionLocal()
    try:
        yield db_session
    finally:
        db_session.close()
