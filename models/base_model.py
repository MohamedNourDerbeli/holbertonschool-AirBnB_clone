#!/usr/bin/python3

"""
Console Base module
"""

import uuid
import datetime
import models


class BaseModel():
    """BaseModel class the parent of other classes"""

    def __init__(self, *args, **kwargs):
        """initializing the public instance attributes"""
        if (kwargs):
            for key, value in (kwargs.items()):
                if (key != "_class_"):
                    if (key == "created_at" or key == "updated_at"):
                        value = datetime.datetime.strptime(
                            value, "%Y-%m-%dT%H:%M:%S.%f")
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            models.storage.new(self)

    # _str_ method
    def __str__(self):
        """method that return string representation of an instance"""
        return f"[{BaseModel.__name__}] ({self.id}) {self.__dict__}"

    # save method
    def save(self):
        """method that updates the public instance attribute
                        *updated_at* with the current datetime"""
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    # to_dict method
    def to_dict(self):
        """method that returns a dictionary containing all
                        keys/values of _dict_ of the instance"""
        dic = {}
        for key, value in (self.__dict__.items()):
            if (isinstance(value, datetime.datetime)):
                value = value.isoformat()
            dic[key] = value
        dic['_class_'] = self.__class__.__name__
        return dic
