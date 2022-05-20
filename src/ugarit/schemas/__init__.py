#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
schemas/__init__

Schemas Init

This is the base schema module.
"""

# -- ALL IMPORTS

# IMPORTANT: Import and add your models here so that it can be created for the schema.
__all__ = ["base", "borrower", "borrower_address", "book_item", "book"]


# -- IMPORTS: SELF

# - Borrower, BorrowerAddress, Base Module
from . import book, book_item, borrower, borrower_address, base
