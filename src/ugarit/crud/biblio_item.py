#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
crud/biblio_item

BiblioItem CRUD Module

This module holds all CRUD Operations for BiblioItem.
"""

# -- IMPORTS: LIBRARIES

# - Standard Libraries
# UUID Imports
from uuid import UUID

# - SQLAlchemy Imports
# SQLAlchemy Session Import
from sqlalchemy.orm import Session

# -- IMPORTS: SELF

# - BiblioItem Schema Import
from ugarit.schemas import biblio_item as schema

# - BiblioItem Model Import
from ugarit.models import biblio_item as model


# CREATE


def create(
    db_session: Session, biblio_item: model.BiblioItemCreate
) -> model.BiblioItem:
    """
    `create`

    Create a BiblioItem

    This function creates a BiblioItem from a given BiblioItemCreate Model.
    """
    new_biblio_item = schema.BiblioItem(
        isbn=biblio_item.isbn,
        issn=biblio_item.issn,
        ean=biblio_item.ean,
        publication_year=biblio_item.publication_year,
        publisher_code=biblio_item.publisher_code,
    )
    db_session.add(new_biblio_item)
    db_session.commit()
    db_session.refresh(new_biblio_item)
    return new_biblio_item


# READ


def get_by_id(db_session: Session, biblio_item_id: UUID) -> model.BiblioItem:
    """
    `get_by_id`

    Get BiblioItem by ID

    This functions returns a borrower from a given Borrower ID as UUID.
    """
    return (
        db_session.query(schema.BiblioItem)
        .filter(schema.BiblioItem.id == biblio_item_id)
        .first()
    )


# UPDATE


def update(
    db_session: Session, biblio_item: model.BiblioItemUpdate
) -> model.BiblioItem:
    """
    Update BiblioItem

    Update a BiblioItem given a BiblioItemUpdate Model.
    """
    update_result = (
        db_session.query(schema.BiblioItem)
        .filter(schema.BiblioItem.id == biblio_item.id)
        .update(
            {
                schema.BiblioItem.isbn: biblio_item.isbn,
                schema.BiblioItem.issn: biblio_item.issn,
                schema.BiblioItem.ean: biblio_item.ean,
                schema.BiblioItem.publication_year: biblio_item.publication_year,
                schema.BiblioItem.publisher_code: biblio_item.publisher_code,
            },
            synchronize_session=True,
        )
    )
    if update_result == 1:
        db_session.commit()
    return update_result == 1
