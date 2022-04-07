from uuid import UUID
from pydantic import BaseModel
from datetime import date


class BorrowerAccountBase(BaseModel):
    id: UUID
    first_name: str | None
    last_name: str | None
    date_of_birth: date | None


class BorrowerAccount(BorrowerAccountBase):
    class Config:
        orm_mode = True


class BorrowerAccountCreate(BorrowerAccountBase):
    pass


class BorrowerAccountUpdate(BorrowerAccountBase):
    pass
