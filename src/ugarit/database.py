#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
database

Database Module

This module sets up database for the App.
"""

# -- IMPORTS: LIBRARIES

# - SQLAlchemy Imports

# SQLAlchemy Engine Import
from sqlalchemy import create_engine

# SQLAlchemy Declarative Base Import
from sqlalchemy.ext.declarative import declarative_base

# SQLAlchemy SessionMaker
from sqlalchemy.orm import sessionmaker

# -- CONSTANTS

DB_URL = "postgresql+psycopg2://dev:dev@127.0.0.1:5432/ugarit"

# -- Create Synchronous Session Engine

engine = create_engine(DB_URL)

# -- Initialize Synchronous Session Maker

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# -- Declare Schema Base Class

Base = declarative_base()
