"""
schemas/__init__

Schemas Init

This is the base schema module.
"""

# -- ALL IMPORTS

# IMPORTANT: Import and add your models here so that it can be created for the schema.
__all__ = ["base", "borrower", "borrower_address", "biblio_item", "biblio"]


# -- IMPORTS: SELF

# - Borrower, BorrowerAddress, Base Module
from . import borrower, borrower_address, base, biblio, biblio_item
