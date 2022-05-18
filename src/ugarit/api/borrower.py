#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
src/ugarit/api/borrower.py

This module holds Borrower API router.
"""

# -- IMPORTS: LIBRARIES

# - Standard Libraries
from uuid import UUID

# - FastAPI Imports
from starlette.status import HTTP_409_CONFLICT
from fastapi import APIRouter, Depends, HTTPException

# - SQLAlchemy Imports
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

# -- IMPORTS: SELF

# - Borrower Model
from ugarit.models import borrower as models_borrower

# - Borrower CRUD
from ugarit.crud import borrower as crud_borrower

# - Database Dependency Injector
from .base import get_db


# - Borrower API Router
#   /borrowers
borrower_router = APIRouter(prefix="/borrowers")


# - CREATE /
@borrower_router.post("/", response_model=models_borrower.Borrower)
def create(
    borrower: models_borrower.BorrowerCreate, db_session: Session = Depends(get_db)
) -> models_borrower.Borrower:
    """
    POST <BODY: BorrowerCreate> /

    Create Borrower

    This creates a single borrower.
    """
    created_borrower = crud_borrower.get_by_email(db_session, borrower.email)
    if created_borrower:
        raise HTTPException(status_code=400, detail="Email Already Registered")
    return crud_borrower.create(db_session, borrower)


# - GET /{id}
@borrower_router.get("/{borrower_id}", response_model=models_borrower.Borrower)
def get_by_id(
    borrower_id: UUID, db_session: Session = Depends(get_db)
) -> models_borrower.Borrower:
    """
    GET /{id:UUID}

    Get a Borrower

    This gets a borrower defined by their UUID.
    """
    return crud_borrower.get_by_id(db_session, borrower_id=borrower_id)


# - PUT /
@borrower_router.put("/", response_model=models_borrower.Borrower)
def update(
    borrower: models_borrower.BorrowerUpdate,
    db_session: Session = Depends(get_db),
) -> models_borrower.Borrower:
    """
    PUT <BODY: BorrowerUpdate>

    Update a borrower

    This updates the borrower defined by the id.
    """
    return crud_borrower.update(db_session, borrower)


# - DELETE /
@borrower_router.delete("/", response_model=bool)
def delete(
    borrower_to_delete: models_borrower.BorrowerDelete,
    db_session: Session = Depends(get_db),
) -> bool:
    """
    DELETE <BODY: BorrowerDelete>

    Delete a Borrower

    This deletes the borrower defined by the id.
    """
    try:
        return crud_borrower.delete(db_session, borrower_to_delete.id)
    except IntegrityError as integrity_err:
        raise HTTPException(
            HTTP_409_CONFLICT,
            detail=f"Borrower Information Not Deleted {borrower_to_delete.id}",
        ) from integrity_err
