#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
crud/borrower

Borrower CRUD Operations

This module holds all CRUD operations for Borrower.
"""


# -- IMPORTS: LIBRARIES

# - Standard Library Imports
from uuid import UUID

# - SQLAlchemy ORM Imports
from sqlalchemy.orm import Session

# -- IMPORTS: PACKAGE

# - Borrower Model Import
from ugarit.models import borrower as model

# - Borrower Schema Import
from ugarit.schemas import borrower as borrower_schema
from ugarit.schemas import borrower_address as borrower_address_schema


# CREATE


def create(db_session: Session, borrower: model.BorrowerCreate) -> model.Borrower:
    """
    Create a Borrower

    This function creates a borrower from a given BorrowerCreate Model.
    """
    new_borrower = borrower_schema.Borrower(
        email=borrower.email,
        first_name=borrower.first_name,
        last_name=borrower.last_name,
        date_of_birth=borrower.date_of_birth,
    )
    db_session.add(new_borrower)
    db_session.commit()
    db_session.refresh(new_borrower)
    return new_borrower


# READ


def get_by_id(db_session: Session, borrower_id: UUID) -> model.Borrower:
    """
    Get Borrower by ID

    This function gets a borrower from a given Borrower ID as UUID.
    """
    return (
        db_session.query(borrower_schema.Borrower)
        .filter(borrower_schema.Borrower.id == borrower_id)
        .first()
    )


def get_by_email(db_session: Session, email_id: str) -> model.Borrower:
    """
    Get Borrower by Email

    This function gets a borrower from a given Email ID.
    """
    return (
        db_session.query(borrower_schema.Borrower)
        .filter(borrower_schema.Borrower.email == email_id)
        .first()
    )


# UPDATE


def update(db_session: Session, borrower: model.BorrowerUpdate) -> bool:
    """
    Update Borrower

    Update a Borrower given a BorrowerUpdate Model.
    """
    update_result = (
        db_session.query(borrower_schema.Borrower)
        .filter(borrower_schema.Borrower.id == borrower.id)
        .update(
            {
                borrower_schema.Borrower.email: borrower.email,
                borrower_schema.Borrower.first_name: borrower.first_name,
                borrower_schema.Borrower.last_name: borrower.last_name,
                borrower_schema.Borrower.date_of_birth: borrower.date_of_birth,
            },
            synchronize_session=False,
        )
    )
    if update_result == 1:
        db_session.commit()
    return update_result == 1


# DELETE


def delete(db_session: Session, borrower_id: UUID) -> bool:
    """
    Delete a Borrower by ID

    Delete a borrower given a Borrower ID as UUID.
    """
    delete_address_result = (
        db_session.query(borrower_address_schema.BorrowerAddress)
        .filter(borrower_address_schema.BorrowerAddress.id == borrower_id)
        .delete()
        == 1
    )
    if delete_address_result:
        db_session.commit()
    delete_result = (
        db_session.query(borrower_schema.Borrower)
        .filter(borrower_schema.Borrower.id == borrower_id)
        .delete()
        == 1
    )
    if delete_result == 1:
        db_session.commit()
    return delete_result == 1
