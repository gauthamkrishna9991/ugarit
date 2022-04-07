from uuid import UUID
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ugarit.models import borrower_address as model
from ugarit.crud import borrower_address as crud
from .base import get_db


borrower_address_router = APIRouter(prefix="/borrower_address")


# CREATE


@borrower_address_router.post("/", response_model=model.BorrowerAddress)
def create(borrower: model.BorrowerAddressCreate, db: Session = Depends(get_db)):
    return crud.create(db, borrower)


# READ


@borrower_address_router.get("/{borrower_id}", response_model=model.BorrowerAddress)
def get_by_id(borrower_id: str, db: Session = Depends(get_db)):
    return crud.get_by_id(db, UUID(borrower_id))
