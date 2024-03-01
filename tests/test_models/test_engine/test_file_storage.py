#!/usr/bin/python3
"""Unit test for the base class base model
"""
import unittest

# import json
from datetime import datetime

# from io import StringIO
# from unittest.mock import patch
from models import base_model
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os
import pip8


class TestBaseClass(unittest.TestCase):
    """TestBaseClass Test the base class
    Args:
        unittest (): Propertys for unit testing
    """

    maxDiff = None

    def setUp(self):
        """condition to test file saving"""
        with open("test.json", "w"):
            FileStorage._FileStorage__file_path = "test.json"
            FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """destroys created file"""
        FileStorage._FileStorage__file_path = "file.json"
        try:
            os.remove("test.json")
        except FileNotFoundError:
            pass

    def test_module_doc(self):
        """check for module documentation"""
        self.assertTrue(len(base_model.__doc__) > 0)

    def test_class_doc(self):
        """check for documentation"""
        self.assertTrue(len(BaseModel.__doc__) > 0)

    def test_method_docs(self):
        """check for method documentation"""
        for func in dir(BaseModel):
            self.assertTrue(len(func.__doc__) > 0)

    def test_pep8(self):
        """test base and test_base for pep8 conformance"""
        style = pep8.StyleGuide(quiet=True)
        file1 = "models/base_model.py"
        file2 = "tests/test_models/test_base_model.py"
        result = style.check_files([file1, file2])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warning)."
        )

    # test_id_type


def test_id_type(self):
    """Test id type"""
    my_third = BaseModel()
    self.assertIsInstance(my_third.id, str)


# test_datetime_type
def test_datetime_type(self):
    """Test datetime type"""
    my_third = BaseModel()
    self.assertIsInstance(my_third.created_at, datetime)


# test_to_dict
def test_to_dict(self):
    """testing to dict function"""
    test = BaseModel()
    my_model = test.to_dict()
    self.assertIsInstance(my_model["created_at"], str)
    self.assertIsInstance(my_model["updated_at"], str)
    self.assertIsInstance(test.created_at, datetime)
    self.assertIsInstance(test.updated_at, datetime)
    self.assertEqual(my_model["created_at"], test.created_at.isoformat())
    self.assertEqual(my_model["updated_at"], test.updated_at.isoformat())


# test_base_from_dict
def test_base_from_dict(self):
    """Testing task 4, with kwargs init"""
    my_model = BaseModel()
    my_model_json = my_model.to_dict()
    my_new_model = BaseModel(**my_model_json)
    self.assertEqual(my_model_json, my_new_model.to_dict())
    self.assertIsInstance(my_new_model.id, str)
    self.assertIsInstance(my_new_model.created_at, datetime)
    self.assertIsInstance(my_new_model.updated_at, datetime)


# test_base_from_emp_dict
def test_base_from_emp_dict(self):
    """test with an empty dictionary"""
    my_dict = {}
    my_new_model = BaseModel(**my_dict)
    self.assertIsInstance(my_new_model.id, str)
    self.assertIsInstance(my_new_model.created_at, datetime)
    self.assertIsInstance(my_new_model.updated_at, datetime)


# test_base_from_non_dict
def test_base_from_non_dict(self):
    """test with a None dictionary"""
    my_new_model = BaseModel(None)
    self.assertIsInstance(my_new_model.id, str)
    self.assertIsInstance(my_new_model.created_at, datetime)
    self.assertIsInstance(my_new_model.updated_at, datetime)
