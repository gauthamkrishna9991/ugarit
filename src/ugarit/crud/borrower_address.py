from uuid import UUID
from fastapi import HTTPException
from sqlalchemy.orm import Session

from ugarit.models import borrower_address as model
from ugarit.schemas import borrower_address as schema

# - BorrowerAddress


# CREATE


def create(db: Session, borrower_addr: model.BorrowerAddress):
    if (
        db.query(schema.BorrowerAddress)
        .filter(schema.BorrowerAddress.id == borrower_addr.id)
        .first()
        is not None
    ):
        raise HTTPException(
            422, f"Address associated with borrower {borrower_addr.id} exists."
        )
    new_borrower = schema.BorrowerAddress(
        id=borrower_addr.id,
        address=borrower_addr.address,
        address2=borrower_addr.address2,
        city=borrower_addr.city,
        state=borrower_addr.state,
        zipcode=borrower_addr.zipcode,
    )
    db.add(new_borrower)
    db.commit()
    db.refresh(new_borrower)
    return new_borrower


# READ


def get_by_id(db: Session, borrower_id: UUID):
    return (
        db.query(schema.BorrowerAddress)
        .filter(schema.BorrowerAddress.id == borrower_id)
        .first()
    )
