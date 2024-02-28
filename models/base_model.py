#!/usr/bin/python3
"""
BaseModel module

This module defines the BaseModel class,
which serves as the base class for other classes.
"""
from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel:
    """
    BaseModel class represents the base model
    for other classes.
    """

    __test = 0

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the BaseModel class.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        if kwargs:
            date_format = "%Y-%m-%dT%H:%M:%S.%f"
            arg = kwargs.copy()
            del arg["__class__"]
            for key in arg:
                if key in {"created_at", "updated_at"}:
                    arg[key] = datetime.strptime(arg[key], date_format)
            self.__dict__ = arg
        else:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            storage.new(self)

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.

        Returns:
            str: String representation.
        """
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the updated_at attribute to the
        current datetime and saves the instance.
        """
        self.updated_at = datetime.utcnow()
        storage.save()

    def to_dict(self):
        """
        Converts the BaseModel instance to a dictionary.

        Returns:
            dict: Dictionary representation of the instance.
        """
        dic = self.__dict__.copy()
        dic["__class__"] = self.__class__.__name__
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()
        return dic
