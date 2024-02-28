#!/usr/bin/python3
"""Module representing the User class."""
from models.base_model import BaseModel
from models import storage


class User(BaseModel):
    """Represents a user in the system."""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self):
        """Initialize a new User instance."""
        super().__init__()
