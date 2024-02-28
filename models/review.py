#!/usr/bin/python3
"""Module representing the Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represents a Review in the system."""

    place_id = ""
    user_id = ""
    text = ""
