#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
models/borrower

Borrower Models Module

This module holds all Borrower Models.
"""

# -- IMPORTS: LIBRARIES

# - Standard Library Imports

# DateTime Imports
from datetime import date

# UUID Imports
from uuid import UUID

# - Pydantic Imports
from pydantic import BaseModel


class BorrowerBase(BaseModel):
    """
    # BorrowerBase Model

    This model holds members that are shared across all instances of Borrower.
    """

    email: str
    first_name: str
    last_name: str
    date_of_birth: date


class Borrower(BorrowerBase):
    """
    # Borrower Model

    This model is parsed and sent back for Borrower.
    """

    id: UUID

    class Config:
        orm_mode = True


class BorrowerCreate(BorrowerBase):
    pass


class BorrowerUpdate(BorrowerBase):
    id: UUID


class BorrowerDelete(BaseModel):
    id: UUID
