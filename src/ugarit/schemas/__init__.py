#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
schemas/__init__

Schemas Module

This module holds all schemas.
"""

# -- ALL IMPORTS

# IMPORTANT: Import and add your models here so that it can be created for the schema.
__all__ = ["base", "book", "book_item", "borrower", "borrower_address"]


# -- IMPORTS: SELF

# - Borrower, BorrowerAddress, Base Module
from . import base, book, book_item, borrower, borrower_address
