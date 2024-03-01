#!/usr/bin/python3
"""Unit test for the file storage class
"""
import unittest
from models.engine import file_storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os
from models import storage


class TestFileStorageClass(unittest.TestCase):
    """TestFileStorage test of suits for the engine
    testing save, all, reload and new methods
    Args:
        unittest (): Propertys for unit testing
    """

    maxDiff = None

    def setUp(self):
        """condition to test file saving"""
        with open("test.json", "w"):
            FileStorage.__file_path = "file.json"
            FileStorage.__objects = {}

    def tearDown(self):
        """destroys created file"""
        FileStorage.__file_path = "file.json"
        try:
            os.remove("test.json")
        except FileNotFoundError:
            pass

    def test_module_doc(self):
        """check for module documentation"""
        self.assertTrue(len(file_storage.__doc__) > 0)

    def test_class_doc(self):
        """check for documentation"""
        self.assertTrue(len(FileStorage.__doc__) > 0)

    def test_method_docs(self):
        """check for method documentation"""
        for func in dir(FileStorage):
            self.assertTrue(len(func.__doc__) > 0)


    def test_all(self):
        """Test method all from filestorage"""
        my_obj = FileStorage()
        my_dict = my_obj.all()
        self.assertTrue(type(my_dict) is dict)

    def test_new(self):
        """Tests method new for filestorage"""
        my_obj = FileStorage()
        new_obj = BaseModel()
        my_obj.new(new_obj)
        my_dict = my_obj.all()
        key = "{}.{}".format(type(new_obj).__name__, new_obj.id)
        self.assertTrue(key in my_dict)

    def test_empty_reload(self):
        """Empty reload function"""
        my_obj = FileStorage()
        new_obj = BaseModel()
        my_obj.new(new_obj)
        my_obj.save()
        my_dict1 = my_obj.all()
        os.remove("test.json")
        my_obj.reload()
        my_dict2 = my_obj.all()
        self.assertTrue(my_dict2 == my_dict1)

    def test_save(self):
        """Tests the save method for filestorage"""
        my_obj = FileStorage()
        new_obj = BaseModel()
        my_obj.new(new_obj)
        my_dict1 = my_obj.all()
        my_obj.save()
        my_obj.reload()
        my_dict2 = my_obj.all()
        for key in my_dict1:
            key1 = key
        for key in my_dict2:
            key2 = key
        self.assertEqual(my_dict1[key1].to_dict(), my_dict2[key2].to_dict())

    def test_instance(self):
        """Check storage"""
        self.assertIsInstance(storage, FileStorage)

    def test_file_path(self):
        """
        Test to see if the file_self.path exist
        """
        try:
            self.assertEqual(FileStorage.__file_path, "file.json")
        except AttributeError:
            pass

    def test_objects_exist_storage(self):
        """
        Test if __objects exist and was created
        """
        dic = storage.all()
        try:
            self.assertEqual(FileStorage.all(), dic)
            self.assertTrue(FileStorage.__objects)
        except AttributeError:
            pass


if __name__ == "__main__":
    unittest.main()
