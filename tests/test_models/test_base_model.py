#!/usr/bin/python3

"""Defines unittests for models/BaseModel.py
unittest classes:
    TestBaseModelInstantiation
    TestBaseModelSave
    TestBaseModelToDict
"""
import unittest
from datetime import datetime
from time import sleep
import os
from models.base_model import BaseModel
import models


class TestBaseModelInstantiation(unittest.TestCase):
    """This class content the unittest of the BaseModel Module
    """
    def test_instance_no_args(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_instance_in_objects(self):
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_public_id_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_public_created_at_datetime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_public_updated_at_dattime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_two_BaseModels_unique_ids(self):
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)

    def test_two_BaseModels_differents_created_at(self):
        bm1 = BaseModel()
        sleep(0.08)
        bm2 = BaseModel()
        self.assertNotEqual(bm1.created_at, bm2.created_at)

    def test_two_BaseModels_differents_updated_at(self):
        bm1 = BaseModel()
        sleep(0.08)
        bm2 = BaseModel()
        self.assertNotEqual(bm1.updated_at, bm2.updated_at)

    def test_args_unused(self):
        bm = BaseModel(None)
        self.assertNotIn(None, bm.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dt = datetime.now()
        dt_iso = dt.isoformat()
        bm = BaseModel(id="34598765", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(bm.id, "34598765")
        self.assertEqual(bm.created_at, dt)
        self.assertEqual(bm.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)


class TestBaseModelSave(unittest.TestCase):
    """Unittest od the save method inside the BaseModel module
    """
    def setUp(self):
        try:
            os.rename("file.json", "tmp.json")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp.json", "file.json")
        except IOError:
            pass

    def test_save(self):
        bm = BaseModel()
        sleep(0.04)
        old_updated_at = bm.updated_at
        bm.save()
        self.assertLess(old_updated_at, bm.updated_at)

    def test_two_save(self):
        bm = BaseModel()
        sleep(0.04)
        old_updated_at = bm.updated_at
        bm.save()
        new_updated_at = bm.updated_at
        self.assertLess(old_updated_at, new_updated_at)
        sleep(0.02)
        bm.save()
        self.assertLess(new_updated_at, bm.updated_at)

    def test_save_with_argument(self):
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.save(None)


class TestBaseModelToDict(unittest.TestCase):
    """This the to dict methode inside the BaseModel module
    """
    def test_to_dict_type(self):
        self.assertEqual(dict, type(BaseModel().to_dict()))

    def test_to_dict_contains_keys(self):
        bm = BaseModel()
        self.assertIn("id", bm.to_dict())
        self.assertIn("created_at", bm.to_dict())
        self.assertIn("updated_at", bm.to_dict())
        self.assertIn("__class__", bm.to_dict())

    def test_to_dict_adds_args(self):
        bm = BaseModel()
        bm.first_name = "Holberton"
        bm.my_number = 89
        self.assertEqual("Holberton", bm.first_name)
        self.assertIn("my_number", bm.to_dict())

    def test_to_dict_type_attributes(self):
        bm = BaseModel()
        p_dict = bm.to_dict()
        self.assertEqual(str, type(p_dict['id']))
        self.assertEqual(str, type(p_dict['created_at']))
        self.assertEqual(str, type(p_dict['updated_at']))

    def test_to_dict_output(self):
        d = datetime.now()
        bm = BaseModel()
        bm.id = "123456"
        bm.created_at = bm.updated_at = d
        tdict = {
            'id': '123456',
            '__class__': 'BaseModel',
            'created_at': d.isoformat(),
            'updated_at': d.isoformat(),
        }
        self.assertDictEqual(bm.to_dict(), tdict)

    def test_to_dict(self):
        bm = BaseModel()
        self.assertNotEqual(bm.to_dict(), bm.__dict__)

    def test_to_dict_with_argument(self):
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.to_dict(None)


if __name__ == "__main__":
    unittest.main()
