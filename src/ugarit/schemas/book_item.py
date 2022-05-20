"""
schemas/book_item

BookItem Schema

This holds the schema required for BookItem
"""

# -- IMPORTS: LIBRARIES

# - Standard Library Imports
import uuid

# - SQLAlchemy
# Column + Types Imports
from sqlalchemy import Column, String, ForeignKey

# PostgreSQL-specific UUID
from sqlalchemy.dialects.postgresql import UUID

# -- IMPORTS: SELF

# - Database Base Imports
from .base import Base


# -- SCHEMA


# pylint: disable=too-few-public-methods
class BookItem(Base):
    """
    BookItem Schema

    This holds SQLAlchemy Schema for BookItem
    """

    # - Table Name
    __tablename__: str = "book_items"

    # - ID
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    # - Book Element
    book = Column(UUID(as_uuid=True), ForeignKey("books.id"))
    # - ISBN Number, for Books
    isbn = Column(String, index=True)
    # - ISSN Number for Periodicals
    issn = Column(String, index=True)
    # - EAN Code for Other Products
    ean = Column(String, index=True)
    # - Publication Year
    publication_year = Column(String, index=True)
    # - Publisher Code
    publisher_code = Column(String, index=True)
