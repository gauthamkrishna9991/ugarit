#!/usr/bin/env python3

"""
models/borrower_address

BorrowerAddress Models Module

This module holds all BorrowerAddress Models.
"""

# -- IMPORTS: LIBRARIES

# - Standard Library Imports

# UUID Import
from uuid import UUID

# - Pydantic Imports
from pydantic import BaseModel


class BorrowerAddressBase(BaseModel):
    """
    BorrowerAddress Base Model
    """

    # - ID for the object, parsed as UUID.
    id: UUID
    # - address     : Address Line 1
    address: str
    # - address2    : Address Line 2
    address2: str
    # - city        : City
    city: str
    # - state       : State
    state: str
    # - country     : Country
    country: str
    # - zipcode     : ZIP Code
    zipcode: str


class BorrowerAddress(BorrowerAddressBase):
    """
    # BorrowerAddress Model

    This model is parsed and sent back for BorrowerAddress.
    """

    class Config:
        orm_mode = True


class BorrowerAddressCreate(BorrowerAddressBase):
    """
    # BorrowerAddressCreate Model

    This model allows you to create a BorrowerAddress object.
    """

    pass


class BorrowerAddressUpdate(BorrowerAddressBase):
    pass
