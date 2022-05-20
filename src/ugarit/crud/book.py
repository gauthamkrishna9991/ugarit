#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
crud/book

Book CRUD Module

This module holds all CRUD Operations for Book.
"""

# -- IMPORTS: LIBRARIES

# - Standard Library Imports
# UUID Import
from uuid import UUID

# - SQLAlchemy Imports
from sqlalchemy.orm import Session

# -- IMPORTS: SELF

# - Book Model
from ugarit.models import book as model

# - Book Schema
from ugarit.schemas import book as schema


# CREATE


def create(db_session: Session, book: model.BookCreate) -> model.Book:
    """
    Create a Book

    This functions creates a book from a given BookCreate Object
    """
    new_book = schema.Book(
        author=book.author,
        title=book.title,
        medium=book.medium,
        part_number=book.part_number,
        part_name=book.part_name,
        subtitle=book.subtitle,
    )
    db_session.add(new_book)
    db_session.commit()
    db_session.refresh(new_book)
    return new_book


# READ


def get_by_id(db_session: Session, book_id: UUID) -> model.Book:
    """
    Get Book by ID

    This function gets a Book from a given Book ID as UUID
    """
    return db_session.query(schema.Book).filter(schema.Book.id == book_id).first()


# UPDATE


def update(db_session: Session, book: model.BookUpdate) -> bool:
    """
    Update a Book given it's ID

    This function updates a book given it's ID
    """
    update_result = (
        db_session.query(schema.Book)
        .filter(schema.Book.id == book.id)
        .update(
            {
                schema.Book.author: book.author,
                schema.Book.title: book.title,
                schema.Book.subtitle: book.subtitle,
                schema.Book.medium: book.medium,
                schema.Book.part_number: book.part_number,
                schema.Book.part_name: book.part_name,
            }
        )
    )
    if update_result == 1:
        db_session.commit()
    return update_result == 1


# DELETE


def delete(db_session: Session, book: model.BookDelete) -> bool:
    """
    Delete a Book given it's ID

    This function deletes a book given it's ID.
    """
    # TODO: Implement referential errors as Books can have related Book Items.
    delete_result = (
        db_session.query(schema.Book).filter(schema.Book.id == book.id).delete()
    )
    print(delete_result)
    if delete_result == 1:
        db_session.commit()
    return delete_result == 1
