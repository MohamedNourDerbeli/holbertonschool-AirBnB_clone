#!/usr/bin/python3
"""Module representing the State class."""
from models.base_model import BaseModel


class City(BaseModel):
    """Represents a City in the system."""

    state_id = ""
    name = ""
