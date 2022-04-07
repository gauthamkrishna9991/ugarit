#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
src/ugarit/crud/borrower_account.py

BorrowerAccount CRUD Operations

This holds all CRUD Operations for BorrowerAccount
"""

# -- IMPORTS: LIBRARIES

# - Standard Libraries
from uuid import UUID

# - FastAPI Imports
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY
from fastapi import HTTPException

# - SQLAlchemy Imports
from sqlalchemy.orm import Session

# -- IMPORTS: PACKAGE

# - Import BorrowerAccount Model
from ugarit.models import borrower_account as model

# - Import BorrowerAccount Schema
from ugarit.schemas import borrower_account as schema

# - Import Borrower CRUD
from ugarit.crud import borrower as borrower_crud


# CREATE


def create(
    db_session: Session, borrower_accnt: model.BorrowerAccountCreate
) -> model.BorrowerAccount:
    """
    Create BorrowerAccount

    This creates a BorrowerAccount Object.
    """
    if (
        db_session.query(schema.BorrowerAccount)
        .filter(schema.BorrowerAccount.id == borrower_accnt.id)
        .first()
        is not None
    ):
        raise HTTPException(
            HTTP_422_UNPROCESSABLE_ENTITY,
            f"Borrower associated with id {borrower_accnt.id} exists.",
        )
    new_borrower_account = schema.BorrowerAccount(
        id=borrower_accnt.id,
        first_name=borrower_accnt.first_name,
        last_name=borrower_accnt.last_name,
    )
    new_borrower_account.borrower = borrower_crud.get_by_id(
        db_session, borrower_accnt.id
    )
    db_session.add(new_borrower_account)
    db_session.commit()
    db_session.refresh(new_borrower_account)
    return new_borrower_account


# READ


def get_by_id(db_session: Session, borrower_id: UUID) -> model.BorrowerAccount:
    """
    Get BorrowerAccount by ID

    This gets a BorrowerAccount Object given its Borrower ID.
    """
    return (
        db_session.query(schema.BorrowerAccount)
        .filter(schema.BorrowerAccount.id == borrower_id)
        .first()
    )


# UPDATE


def update_from_id(
    db_session: Session, borrower_data: model.BorrowerAccountUpdate
) -> model.BorrowerAccount:
    """
    Update BorrowerAccount

    This updates a BorrowerAccount Object given an ID.
    """
    update_result = (
        db_session.query(schema.BorrowerAccount)
        .filter(schema.BorrowerAccount.id == borrower_data.id)
        .update(
            {
                schema.BorrowerAccount.first_name: borrower_data.first_name,
                schema.BorrowerAccount.last_name: borrower_data.last_name,
                schema.BorrowerAccount.date_of_birth: borrower_data.date_of_birth,
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
    Delete BorrowerAccount by ID

    This Deletes a BorrowerAccount Object given the Borrower ID.
    """
    delete_result = (
        db_session.query(schema.BorrowerAccount.id == borrower_id).delete() == 1
    )
    if delete_result == 1:
        db_session.commit()
    return delete_result == 1
