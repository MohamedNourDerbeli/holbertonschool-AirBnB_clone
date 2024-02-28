#!/usr/bin/python3
"""Module representing the User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """Represents a user in the system."""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
