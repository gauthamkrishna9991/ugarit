"""
API Base Module

This holds all API Objects
"""

# Objects Exported Publically
__all__ = ["base"]


# -- IMPORTS: LIBRARIES

# - FastAPI Imports
from fastapi import APIRouter

# -- IMPORTS: PACKAGE

# - Base API Module
from . import base
# - Borrower API Router
from . import borrower
# - BorrowerAccount API Router
from . import borrower_account
# - BorrowerAddress API Router
from . import borrower_address


# - Inititalize API Router
api_router = APIRouter(prefix="/api")

# - Include Borrower Router
api_router.include_router(borrower.borrower_router)

# - Include BorrowerAccount Router
api_router.include_router(borrower_account.borrower_account_router)

# - Include BorrowerAddress Router
api_router.include_router(borrower_address.borrower_address_router)
