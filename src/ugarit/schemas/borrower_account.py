from sqlalchemy import Column, String, ForeignKey, Date
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from .base import Base


class BorrowerAccount(Base):
    __tablename__: str = "borrower_accounts"

    id = Column(UUID(as_uuid=True), ForeignKey("borrowers.id"), primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    date_of_birth = Column(Date)

    borrower = relationship("Borrower", back_populates="account", uselist=False)
