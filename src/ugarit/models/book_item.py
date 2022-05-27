#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
models/book_item

BookItem Models Module

This module has all BookItem HTTP Models.
"""

# -- IMPORTS: LIBRARIES

# - Standard Library Imports
# Date-Time
from datetime import date, datetime

# Typing Imports: Optional
from typing import Optional

# UUID Imports
from uuid import UUID

# - Pydantic Imports
from pydantic import BaseModel


# -- MODELS


class BookItemBase(BaseModel):
    """
    BookItem Base Model

    This holds HTTP Model for BookItem.
    """

    # - Book ID
    book: Optional[UUID]
    # - ISBN Number, for Books
    isbn: Optional[str]
    # - ISSN Number, for Periodicals
    issn: Optional[str]
    # - EAN Code, for Other Products
    ean: Optional[str]
    # - Publication Year
    publication_year: Optional[str]
    # - Publisher Code
    publisher_code: Optional[str]


class BookItem(BookItemBase):
    """
    # BookItem Model

    This model is parsed and sent back for BookItem.
    """

    # - ID
    id: UUID
    # - Last Updated
    last_updated: datetime
    # - Created
    created: date

    # pylint: disable=too-few-public-methods
    class Config:
        """
        Config for BookItem

        Enable ORM Mode.
        """

        orm_mode = True


class BookItemCreate(BookItemBase):
    """
    # BookItemCreate Model

    *Type*: **Response**

    This is used to create BookItem from given HTTP Request.
    """


class BookItemUpdate(BookItemBase):
    """
    # BookItemUpdate Model

    This is used to update a BookItem object, given a valid UUID.
    """

    # - ID
    id: UUID
