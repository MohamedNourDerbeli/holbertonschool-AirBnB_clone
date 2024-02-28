#!/usr/bin/python3
"""
File Storage module

This module defines the FileStorage class, which handles serialization and deserialization of objects to and from JSON files.
"""

import json
from os.path import isfile


class FileStorage:
    """
    FileStorage class manages serialization and deserialization of objects to and from JSON files.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects.

        Returns:
            dict: Dictionary containing all objects stored.
        """
        return self.__objects

    def new(self, obj):
        """
        Adds a new object to the __objects dictionary.

        Args:
            obj: Object to add.
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to a JSON file.
        """
        dic_data = {}
        with open(self.__file_path, "w", encoding="utf-8") as File:
            for key, obj in self.__objects.items():
                dic_data[key] = obj.to_dict()
            File.write(json.dumps(dic_data))

    def reload(self):
        """
        Deserializes JSON file to __objects.
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        if isfile(self.__file_path):
            with open(self.__file_path, "r") as file:
                load_objects = json.load(file)
                for key, value in load_objects.items():
                    class_name, class_id = key.split(".")
                    obj_class = eval(class_name)
                    self.__objects[key] = obj_class(**value)
