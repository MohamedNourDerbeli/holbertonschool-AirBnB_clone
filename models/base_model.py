#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Represents the BaseModel """
    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def save(self):
        """ updated_at take the current datetime."""
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """
        Return the dictionary of the BaseModel instance.
        """
        chaima = self.__dict__.copy()
        chaima["__class__"] = self.__class__.__name__
        chaima["created_at"] = self.created_at.isoformat()
        chaima["updated_at"] = self.updated_at.isoformat()

        return chaima

    def __str__(self):
        """Return the string representation of the BaseModel instance."""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
