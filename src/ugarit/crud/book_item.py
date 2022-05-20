#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
crud/book_item

= CRUD Module

This module holds all CRUD Operations for BookItem.
"""

# -- IMPORTS: LIBRARIES

# - Standard Libraries
# UUID Imports
from uuid import UUID

# - SQLAlchemy Imports
# SQLAlchemy Session Import
from sqlalchemy.orm import Session

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
        isbn=book_item.isbn,
        issn=book_item.issn,
        ean=book_item.ean,
        publication_year=book_item.publication_year,
        publisher_code=book_item.publisher_code,
    )
    db_session.add(new_book_item)
    db_session.commit()
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


def update(db_session: Session, book_item: model.BookItemUpdate) -> model.BookItem:
    """
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
            },
            synchronize_session=True,
        )
    )
    if update_result == 1:
        db_session.commit()
    return update_result == 1
