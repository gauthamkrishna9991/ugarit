"""
schema/borrower

Borrower Schema

This holds the schema for Borrower
"""

# -- IMPORTS: LIBRARIES

# - UUID
import uuid

# - SQLAlchemy Imports
# Column + Types Imports
from sqlalchemy import Column, String, Date

# PostgreSQL-specific UUID Import
from sqlalchemy.dialects.postgresql import UUID

# -- IMPORTS: SELF
from ugarit.database import Base


# -- SCHEMA
class Borrower(Base):
    """
    Borrower Schema

    This holds SQLAlchemy Schema for Borrower
    """

    __tablename__: str = "borrowers"

    # ID of the borrower (UUID type)
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    # Email ID of Borrower (organization given or personal, NEEDS TO BE UNIQUE)
    email = Column(String, unique=True, nullable=False)
    # First Name of Borrower
    first_name = Column(String)
    # Last Name of Borrower
    last_name = Column(String)
    # Date of Birth
    date_of_birth = Column(Date)
