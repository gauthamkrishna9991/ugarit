from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from .base import Base


class BorrowerAddress(Base):
    __tablename__: str = "borrower_addresses"

    id = Column(UUID(as_uuid=True), ForeignKey("borrowers.id"), primary_key=True)
    address = Column(String)
    address2 = Column(String)
    city = Column(String)
    state = Column(String)
    country = Column(String)
    zipcode = Column(String)

    borrower = relationship("Borrower", uselist=False)
