#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
crud/book_item

CRUD Module

This module holds all CRUD Operations for BookItem.
"""

# -- IMPORTS: LIBRARIES

# - Standard Libraries
# Datetime Imports
from datetime import datetime

# UUID Imports
from uuid import UUID

# - SQLAlchemy Imports
# SQLAlchemy Session Import
from sqlalchemy.orm import Session

# SQLAlchemy Error
from sqlalchemy.exc import IntegrityError

# - FastAPI Imports
# FastAPI Exception
from fastapi.exceptions import HTTPException

# - Starlette Imports
# Status Code
from starlette.status import HTTP_409_CONFLICT

# -- IMPORTS: SELF

# - BookItem Schema Import
from ugarit.schemas import book_item as schema

# - BookItem Model Import
from ugarit.models import book_item as model


# CREATE


def create(db_session: Session, book_item: model.BookItemCreate) -> model.BookItem:
    """
    `create`

    Create a BookItem

    This function creates a BookItem from a given BookItemCreate Model.
    """
    new_book_item = schema.BookItem(
        book=book_item.book,
        isbn=book_item.isbn,
        issn=book_item.issn,
        ean=book_item.ean,
        publication_year=book_item.publication_year,
        publisher_code=book_item.publisher_code,
        last_updated=datetime.utcnow(),
        created=datetime.utcnow(),
    )
    db_session.add(new_book_item)
    try:
        # Try to commit the changes.
        db_session.commit()
    except IntegrityError as integrity_err:
        if "book" in integrity_err.params:
            book = integrity_err.params["book"]
            if book is None:
                #  TODO: Raise better exceptions
                raise HTTPException(HTTP_409_CONFLICT, "Book is not given")
            # TODO: Raise Better Exceptions
            raise HTTPException(
                HTTP_409_CONFLICT, f"Book with ID '{book}' does not exist."
            )
        # For now raise the caught exception.
        raise integrity_err
    db_session.refresh(new_book_item)
    return new_book_item


# READ


def get_by_id(db_session: Session, book_item_id: UUID) -> model.BookItem:
    """
    `get_by_id`

    Get BookItem by ID

    This functions returns a borrower from a given Borrower ID as UUID.
    """
    return (
        db_session.query(schema.BookItem)
        .filter(schema.BookItem.id == book_item_id)
        .first()
    )


# UPDATE


def update(db_session: Session, book_item: model.BookItemUpdate) -> bool:
    """
    `update`

    Update BookItem

    Update a BookItem given a BookItemUpdate Model.
    """
    update_result = (
        db_session.query(schema.BookItem)
        .filter(schema.BookItem.id == book_item.id)
        .update(
            {
                schema.BookItem.isbn: book_item.isbn,
                schema.BookItem.issn: book_item.issn,
                schema.BookItem.ean: book_item.ean,
                schema.BookItem.publication_year: book_item.publication_year,
                schema.BookItem.publisher_code: book_item.publisher_code,
                schema.BookItem.last_updated: datetime.utcnow(),
            },
            synchronize_session=False,
        )
    )
    try:
        if update_result == 1:
            db_session.commit()
        return update_result == 1
    except IntegrityError as integrity_err:
        raise HTTPException(
            HTTP_409_CONFLICT, f"INTEGRITY ERROR: {integrity_err.detail}"
        ) from integrity_err
