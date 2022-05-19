"""
schemas/biblio

Biblio Schema

This holds the schema required for Biblio.
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


# - SCHEMA
class Biblio(Base):
    """
    Biblio Schema

    This holds the SQLAlchemy Schema for Biblio
    """

    __tablename__ = "biblios"

    # ID
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    # Title
    title = Column(String)
    # Subtitle
    subtitle = Column(String)
