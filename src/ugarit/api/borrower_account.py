from uuid import UUID
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ugarit.models import borrower_account as model
from ugarit.crud import borrower_account as crud
from .base import get_db

borrower_account_router = APIRouter(prefix="/borrower_accounts")


# CREATE


@borrower_account_router.post("/", response_model=model.BorrowerAccountCreate)
def create(borrower: model.BorrowerAccountCreate, db: Session = Depends(get_db)):
    return crud.create(db, borrower)


# READ


@borrower_account_router.get("/{borrower_id}", response_model=model.BorrowerAccount)
def get_by_id(borrower_id: str, db: Session = Depends(get_db)):
    return crud.get_by_id(db, UUID(borrower_id))


# UPDATE


@borrower_account_router.put("/", response_model=bool)
def update(new_borrower: model.BorrowerAccountUpdate, db: Session = Depends(get_db)):
    return crud.update_from_id(db, new_borrower)


# DELETE: NOT NEEDED HERE
