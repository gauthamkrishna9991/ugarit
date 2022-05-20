#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
schemas/book

Book Schema

This holds the schema required for Book.
"""

# -- IMPORTS: LIBRARIES

# - Standard Library Imports
import uuid

# - SQLAlchemy
# Columns + Types Imports
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID


# -- IMPORTS: SELF

# - Database Base Imports
from ugarit.database import Base


# -- SCHEMA


# pylint: disable=too-few-public-methods
class Book(Base):
    """
    Book Schema

    This holds the SQLAlchemy Schema for Book
    """

    __tablename__ = "books"

    # ID
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    # Author
    author = Column(String)
    # Title
    title = Column(String)
    # Subtitle
    subtitle = Column(String)
    # Medium
    medium = Column(String)
    # Part Number
    part_number = Column(String)
    # Part Name
    part_name = Column(String)
