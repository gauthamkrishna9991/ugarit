#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
models/biblio_item

BiblioItem Models Module

This module has all BiblioItem HTTP Models.
"""

# -- IMPORTS: LIBRARIES

# - Standard Library Imports
# UUID Imports
from typing import Optional
from uuid import UUID

# - Pydantic Imports
from pydantic import BaseModel


class BiblioItemBase(BaseModel):
    """
    BiblioItem Base Model

    This holds HTTP Model for BiblioItem.
    """

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


class BiblioItem(BiblioItemBase):
    """
    # BiblioItem Model

    This model is parsed and sent back for BiblioItem.
    """

    # - ID
    id: UUID

    class Config:
        """
        Config for BiblioItem

        Enable ORM Mode.
        """

        orm_mode = True


class BiblioItemCreate(BiblioItemBase):
    """
    # BiblioItemCreate Model

    *Type*: **Response**

    This is used to create BiblioItem from given HTTP Request.
    """

    pass


class BiblioItemUpdate(BiblioItemBase):
    """
    # BiblioItemUpdate Model

    This is used to update a BiblioItem object, given a valid UUID.
    """

    # - ID
    id: UUID
