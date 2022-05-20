#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
api/borrower_address

BorrowerAddress API Module

This module holds API Router for BorrowerAddress.
"""

# -- IMPORTS: LIBRARIES

# - Standard Library Imports
# UUID Import
from uuid import UUID

# - FastAPI Imports
# APIRouter, Depends
from fastapi import APIRouter, Depends

# - SQLAlchemy Imports
# Session ORM
from sqlalchemy.orm import Session


# -- IMPORTS: SELF

# - BorrowerAddress Model Import
from ugarit.models import borrower_address as model

# - BorrowerAddress CRUD Import
from ugarit.crud import borrower_address as crud

# - Database Dependency Injector
from .base import get_db


# -- INITIALIZE ROUTER


borrower_address_router = APIRouter(prefix="/borrower_address")


# CREATE


@borrower_address_router.post("/", response_model=model.BorrowerAddress)
def create(
    borrower: model.BorrowerAddressCreate, db_session: Session = Depends(get_db)
) -> model.BorrowerAddress:
    """
    POST / <BODY: BorrowerAddressCreate>

    Create a BorrowerAddress Object.
    """
    return crud.create(db_session, borrower)


# READ


@borrower_address_router.get("/{borrower_id}", response_model=model.BorrowerAddress)
def get_by_id(
    borrower_id: UUID, db_session: Session = Depends(get_db)
) -> model.BorrowerAddress | None:
    """
    GET /{borrower_id:uuid}

    Return a BorrowerAddress Object, provided it's ID.
    """
    return crud.get_by_id(db_session, borrower_id)
