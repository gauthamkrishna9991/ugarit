#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
api/biblio_item

BiblioItem API Router Module

This module holds API Router for BiblioItem.
"""

# -- IMPORTS: LIBRARIES

# - Standard Libary Imports
from uuid import UUID

# - SQLAlchemy Imports
from sqlalchemy.orm import Session

# - FastAPI Imports
from fastapi import APIRouter, Depends


# -- IMPORTS: SELF

# - Borrower Model
from ugarit.models import biblio_item as model

# - Borrower CRUD
from ugarit.crud import biblio_item as crud

# - Database Dependency Injector
from .base import get_db


# -- BiblioItem API Router
biblio_item_router = APIRouter(prefix="/biblio_item")


# - READ


@biblio_item_router.get(
    "/{biblio_item_id}",
    response_model=model.BiblioItem,
    name="Get BiblioItem by ID",
)
def get_by_id(
    biblio_item_id: UUID, db_session: Session = Depends(get_db)
) -> model.BiblioItem:
    """
    GET  /{id:UUID}

    Get a BiblioItem

    This gets a biblio item referred by its UUID.
    """
    return crud.get_by_id(db_session, biblio_item_id)


# - CREATE


@biblio_item_router.post("/", response_model=model.BiblioItem)
def create(
    biblio_item: model.BiblioItemCreate, db_session: Session = Depends(get_db)
) -> model.BiblioItem:
    """
    POST /

    Create a BiblioItem

    This creates a biblio item from the request.
    """
    return crud.create(db_session, biblio_item)


# - UPDATE


@biblio_item_router.put("/", response_model=model.BiblioItem)
def update(
    biblio_item: model.BiblioItemUpdate, db_session: Session = Depends(get_db)
) -> model.BiblioItem:
    """
    POST /

    Update a BiblioItem
    """
    return crud.update(db_session, biblio_item)
