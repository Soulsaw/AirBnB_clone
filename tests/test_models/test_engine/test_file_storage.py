#!/usr/bin/python3

"""Defines unittests for models/file_storage.py
unittest classes:
    TestFileStorageInstantiation
    TestFileStorageSave
    TestFileStorageToDict
"""
import unittest
from datetime import datetime
from time import sleep
import os
from models.engine.file_storage import FileStorage
import models


class TestFileStorageInstantiation(unittest.TestCase):
    """This class content the unittest of the FileStorage Module
    """
    def test_instance_no_args(self):
        self.assertEqual(FileStorage, type(FileStorage()))

    def test_public_file_path_str(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test_public_objects_dict(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))


if __name__ == "__main__":
    unittest.main()
