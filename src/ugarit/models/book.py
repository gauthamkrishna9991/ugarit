#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
models/book

Book Models

This holds all information required for the model "Book".
"""

# -- IMPORTS: LIBRARIES

# - Standard Library Imports

# Typing Imports
from typing import Optional

# UUID Imports
from uuid import UUID

# - Pydantic Imports
from pydantic import BaseModel


# -- MODELS


class BookBase(BaseModel):
    """
    BookBase Model

    This holds HTTP Model for Book
    """

    # Author
    author: Optional[str]
    # Title
    title: Optional[str]
    # Medium
    medium: Optional[str]
    # Part Number
    part_number: Optional[str]
    # Part Name
    part_name: Optional[str]
    # Subtitle
    subtitle: Optional[str]


class Book(BookBase):
    """
    Book Model

    This holds Response for Book.
    """

    id: UUID

    class Config:
        """
        Configuration for Book Model
        """

        orm_mode = True


class BookCreate(BookBase):
    """
    BookCreate Model

    This model is used for Creating a Book Object.
    """


class BookUpdate(BookBase):
    """
    BookUpdate Model

    This model is used to update a Book Object.
    """

    id: UUID


class BookDelete(BaseModel):
    """
    BookDelete Model

    This model is used to delete a Book Object.
    """

    id: UUID
