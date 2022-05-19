#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
api/auth

API Authentication Module

This module holds everything required for API Authentication.
"""

# -- IMPORTS: LIBRARIES

# - FastAPI Imports
# APIRouter Import
from fastapi import APIRouter

# -- INITIALIZE ROUTER

auth_router = APIRouter(prefix="/auth")
