from uuid import UUID
from pydantic import BaseModel
from datetime import date

# from ugarit.models.borrower_account import BorrowerAccount
# from ugarit.models.borrower_address import BorrowerAddress


class BorrowerBase(BaseModel):
    email: str
    first_name: str
    last_name: str
    date_of_birth: date


class Borrower(BorrowerBase):
    id: UUID

    class Config:
        orm_mode = True


class BorrowerCreate(BorrowerBase):
    pass


class BorrowerUpdate(BorrowerBase):
    id: UUID


class BorrowerDelete(BaseModel):
    id: UUID
