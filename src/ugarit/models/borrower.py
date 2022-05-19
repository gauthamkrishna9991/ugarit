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

    # pylint: disable=too-few-public-methods
    class Config:
        """
        Config

        Module configuration for Borrower.
        """

        orm_mode = True


class BorrowerCreate(BorrowerBase):
    """
    # BorrowerCreate Model

    This model is used to deserizalize POST Request.
    """


class BorrowerUpdate(BorrowerBase):
    """
    # BorrowerUpdate Model

    This model is used to Deseriazlize PUT Request.
    """

    id: UUID


class BorrowerDelete(BaseModel):
    """
    # BorrowerDelete Model

    This model is used to Delete Borrower element. It only takes in a UUID.
    """

    id: UUID
