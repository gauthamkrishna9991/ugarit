from uuid import UUID
from pydantic import BaseModel


class BorrowerAddressBase(BaseModel):
    id: UUID
    address: str
    address2: str
    city: str
    state: str
    country: str
    zipcode: str


class BorrowerAddress(BorrowerAddressBase):
    class Config:
        orm_mode = True


class BorrowerAddressCreate(BorrowerAddressBase):
    pass


class BorrowerAddressUpdate(BorrowerAddressBase):
    pass
