import uuid

from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from ugarit.database import Base


class Borrower(Base):
    __tablename__: str = "borrowers"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String, unique=True, nullable=False)

    account = relationship("BorrowerAccount", uselist=False)
    address = relationship("BorrowerAddress", uselist=False)
