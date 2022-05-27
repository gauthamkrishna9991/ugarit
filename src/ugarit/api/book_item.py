#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
api/book_item

BookItem API Router Module

This module holds API Router for BookItem.
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
from ugarit.models import book_item as model

# - Borrower CRUD
from ugarit.crud import book_item as crud

# - Database Dependency Injector
from .base import get_db


# -- BookItem API Router
book_item_router = APIRouter(prefix="/book_item")


# - READ


@book_item_router.get(
    "/{book_item_id}",
    response_model=model.BookItem,
    name="Get BookItem by ID",
)
def get_by_id(
    book_item_id: UUID, db_session: Session = Depends(get_db)
) -> model.BookItem:
    """
    GET  /{id:UUID}

    Get a BookItem

    This gets a BookItem referred by its UUID.
    """
    return crud.get_by_id(db_session, book_item_id)


# - CREATE


@book_item_router.post("/", response_model=model.BookItem)
def create(
    book_item: model.BookItemCreate, db_session: Session = Depends(get_db)
) -> model.BookItem:
    """
    POST /

    Create a BookItem

    This creates a BookItem from the request.
    """
    return crud.create(db_session, book_item)


# - UPDATE


@book_item_router.put("/", response_model=bool)
def update(
    book_item: model.BookItemUpdate, db_session: Session = Depends(get_db)
) -> bool:
    """
    PUT /

    Update a BookItem
    """
    return crud.update(db_session, book_item)
