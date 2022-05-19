#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
crud/borrower_address

BorrowerAddress CRUD Module

This module holds all CRUD Operations for BorrowerAddress
"""

# -- IMPORTS: LIBRARIES

# - Standard Libraries
# UUID Imports
from uuid import UUID

# - Starlette Imports
from starlette.status import HTTP_409_CONFLICT

# - FastAPI Imports
from fastapi import HTTPException

# - SQLAlchemy Imports
from sqlalchemy.orm import Session


# -- IMPORTS: SELF

# - BorrowerAddress Model Import
from ugarit.models import borrower_address as model

# -- Borrower Model Import
from ugarit.schemas import borrower as borrower_schema

# - BorrowerAddress Schema Import
from ugarit.schemas import borrower_address as schema


# CREATE


def create(
    db_session: Session, borrower_addr: model.BorrowerAddressCreate
) -> model.BorrowerAddress:
    """
    create

    Create a BorrowerAddress Object, given BorrowerAddressCreate model.
    """
    if (
        db_session.query(borrower_schema.Borrower)
        .filter(borrower_schema.Borrower.id == borrower_addr.id)
        .first()
        is None
    ):
        raise HTTPException(
            HTTP_409_CONFLICT,
            f"Borrower with ID {borrower_addr.id} does not exist.",
        )
    if (
        db_session.query(schema.BorrowerAddress)
        .filter(schema.BorrowerAddress.id == borrower_addr.id)
        .first()
        is not None
    ):
        raise HTTPException(
            422, f"Address associated with borrower {borrower_addr.id} exists."
        )
    new_borrower_addr = schema.BorrowerAddress(
        id=borrower_addr.id,
        address=borrower_addr.address,
        address2=borrower_addr.address2,
        city=borrower_addr.city,
        state=borrower_addr.state,
        country=borrower_addr.country,
        zipcode=borrower_addr.zipcode,
    )
    db_session.add(new_borrower_addr)
    db_session.commit()
    db_session.refresh(new_borrower_addr)
    return new_borrower_addr


# READ


def get_by_id(db_session: Session, borrower_id: UUID) -> model.BorrowerAddress | None:
    """
    get_by_id

    Get a BorrowerAddress element by ID.
    """
    return (
        db_session.query(schema.BorrowerAddress)
        .filter(schema.BorrowerAddress.id == borrower_id)
        .first()
    )
