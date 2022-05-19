"""
schemas/biblio_item

BiblioItem Schema

This holds the schema required for BilbioItem
"""

# -- IMPORTS: LIBRARIES

# - Standard Library Imports
import uuid

# - SQLAlchemy
# Column + Types Imports
from sqlalchemy import Column, String

# PostgreSQL-specific UUID
from sqlalchemy.dialects.postgresql import UUID

# -- IMPORTS: SELF

# - Database Base Imports
from ugarit.database import Base


# - SCHEMA
class BiblioItem(Base):
    """
    BiblioItem Schema

    This holds SQLAlchemy Schema for BiblioItem
    """

    # - Table Name
    __tablename__: str = "biblio_items"

    # - ID
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
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
