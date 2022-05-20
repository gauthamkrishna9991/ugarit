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
from starlette.status import HTTP_409_CONFLICT, HTTP_422_UNPROCESSABLE_ENTITY

# - FastAPI Imports
from fastapi import HTTPException

# - SQLAlchemy Imports
# ORM Session Import
from sqlalchemy.orm import Session
# IntegrityError Import
from sqlalchemy.exc import IntegrityError


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
    # Check whether a borrower associated with given ID does not exist.
    if (
        db_session.query(borrower_schema.Borrower)
        .filter(borrower_schema.Borrower.id == borrower_addr.id)
        .first()
        is None
    ):
        # If a borrower exists, return a 409 Conflict Error detailing the error.
        raise HTTPException(
            HTTP_409_CONFLICT,
            f"Borrower with ID {borrower_addr.id} does not exist.",
        )
    # Check whether address for the given ID exists, if so, then we can't "create"
    # this address object.
    if (
        db_session.query(schema.BorrowerAddress)
        .filter(schema.BorrowerAddress.id == borrower_addr.id)
        .first()
        is not None
    ):
        # If there is an existing address for the given ID, return a 422 Unprocessable
        # Entity Error detailing the error.
        raise HTTPException(
            HTTP_422_UNPROCESSABLE_ENTITY,
            f"Address associated with borrower {borrower_addr.id} exists.",
        )
    # If all the above checks are met, create the object.
    new_borrower_addr = schema.BorrowerAddress(
        id=borrower_addr.id,
        address=borrower_addr.address,
        address2=borrower_addr.address2,
        city=borrower_addr.city,
        state=borrower_addr.state,
        country=borrower_addr.country,
        zipcode=borrower_addr.zipcode,
    )
    try:
        db_session.add(new_borrower_addr)
        db_session.commit()
        db_session.refresh(new_borrower_addr)
    except IntegrityError as integrity_err:
        raise HTTPException(
            HTTP_409_CONFLICT,
            f"Address associated with borrower {borrower_addr.id} exists.",
        ) from integrity_err
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


# UPDATE


def update(db_session: Session, borrower_address: model.BorrowerAddressUpdate) -> bool:
    """
    update

    Update a BorrowerAddress element given new data.
    """
    update_result = (
        db_session.query(schema.BorrowerAddress)
        .filter(schema.BorrowerAddress.id == borrower_address.id)
        .update(
            {
                schema.BorrowerAddress.address: borrower_address.address,
                schema.BorrowerAddress.address2: borrower_address.address2,
                schema.BorrowerAddress.city: borrower_address.city,
                schema.BorrowerAddress.state: borrower_address.state,
                schema.BorrowerAddress.country: borrower_address.country,
                schema.BorrowerAddress.zipcode: borrower_address.zipcode,
            },
            synchronize_session=False,
        )
    )
    if update_result == 1:
        db_session.commit()
    return update_result == 1
