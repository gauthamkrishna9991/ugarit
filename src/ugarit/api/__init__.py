#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
API Base Module

This holds all API Objects
"""

# Objects Exported Publically
__all__ = ["base", "api_router"]


# -- IMPORTS: LIBRARIES

# - FastAPI Imports
from fastapi import APIRouter

# -- IMPORTS: PACKAGE

# - Base API Module
from . import base

# - Borrower API Router
from . import borrower

# - BorrowerAddress API Router
from . import borrower_address

# - BookItem API Router
from . import book_item

# - Book API Router
from . import book

# - Inititalize API Router
api_router = APIRouter(prefix="/api")

# - Include Borrower Router
api_router.include_router(borrower.borrower_router)

# - Include BorrowerAddress Router
api_router.include_router(borrower_address.borrower_address_router)

# - Include Book Router
api_router.include_router(book.book_router)

# - Include BookItem Router
api_router.include_router(book_item.book_item_router)
