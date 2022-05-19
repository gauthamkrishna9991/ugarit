"""
schemas/borrower_address

BorrowerAddress Schema

This holds the schema for BorrowerAddress
"""

# -- IMPORTS: LIBRARIES

# - SQLAlchemy Imports
# Column + Types Imports
from sqlalchemy import Column, String, ForeignKey

# PostgreSQL-specific UUID Import
from sqlalchemy.dialects.postgresql import UUID

# ORM Relationship Import
from sqlalchemy.orm import relationship


# -- IMPORTS: SELF

# - Base Model Import
from .base import Base


# - SCHEMA
class BorrowerAddress(Base):
    """
    BorrowerAddress Schema

    This holds SQLAlchemy Schema for BorrowerAddress
    """

    # DB Table Name
    __tablename__: str = "borrower_addresses"

    id = Column(UUID(as_uuid=True), ForeignKey("borrowers.id"), primary_key=True)
    address = Column(String)
    address2 = Column(String)
    city = Column(String)
    state = Column(String)
    country = Column(String)
    zipcode = Column(String)

    borrower = relationship("Borrower", uselist=False)
