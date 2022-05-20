#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
api/book

Book API Module

This module holds API Router for Book.
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

# - Book Model Import
from ugarit.models import book as model

# - Book CRUD Import
from ugarit.crud import book as crud

# - Database Dependency Injector
from .base import get_db


# -- INITIALIZE ROUTER


book_router = APIRouter(prefix="/book")


# CREATE


@book_router.post("/", response_model=model.Book)
def create(book: model.BookCreate, db_session: Session = Depends(get_db)) -> model.Book:
    """
    POST / <BODY: BookCreate>

    Create a Book Object.
    """
    return crud.create(db_session, book)


# READ


@book_router.get("/{book_id}", response_model=model.Book)
def get_by_id(
    book_id: UUID, db_session: Session = Depends(get_db)
) -> model.Book | None:
    """
    GET /{book_id:uuid}

    Return a Book Object, provided it's ID.
    """
    return crud.get_by_id(db_session, book_id)


# UPDATE


@book_router.put("/", response_model=bool)
def update(book: model.BookUpdate, db_session: Session = Depends(get_db)) -> bool:
    """
    PUT /

    Update the Book Object referenced by the ID.
    """
    return crud.update(db_session, book)


# DELETE


@book_router.delete("/", response_model=bool)
def delete(book: model.BookDelete, db_session: Session = Depends(get_db)) -> bool:
    """
    DELETE /

    Delete the Book Object referenced by the ID.
    """
    return crud.delete(db_session, book)
