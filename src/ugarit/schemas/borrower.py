import uuid

from sqlalchemy import Column, String, Date
# from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from ugarit.database import Base


class Borrower(Base):
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

    # address = relationship("BorrowerAddress", backref="borrower")
