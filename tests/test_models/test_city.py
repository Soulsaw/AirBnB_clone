#!/usr/bin/python3

"""Defines unittests for models/city.py
unittest classes:
    TestCityInstantiation
    TestCitySave
    TestCityToDict
"""

import unittest
from datetime import datetime
from time import sleep
import os
from models.city import City
import models


class TestCityInstantiation(unittest.TestCase):
    """This class content the unittest of the City Module
    """
    def test_instance_no_args(self):
        self.assertEqual(City, type(City()))

    def test_instance_in_objects(self):
        self.assertIn(City(), models.storage.all().values())

    def test_public_id_str(self):
        self.assertEqual(str, type(City().id))

    def test_public_created_at_datetime(self):
        self.assertEqual(datetime, type(City().created_at))

    def test_public_updated_at_dattime(self):
        self.assertEqual(datetime, type(City().updated_at))

    def test_state_id_is_public_attribute(self):
        ct = City()
        self.assertEqual(str, type(ct.id))
        self.assertIn("state_id", dir(ct))
        self.assertNotIn("state_id", ct.__dict__)

    def test_name_is_public_attribute(self):
        ct = City()
        self.assertEqual(str, type(ct.id))
        self.assertIn("name", dir(ct))
        self.assertNotIn("name", ct.__dict__)

    def test_two_Citys_unique_ids(self):
        ct1 = City()
        ct2 = City()
        self.assertNotEqual(ct1.id, ct2.id)

    def test_two_Citys_differents_created_at(self):
        ct1 = City()
        sleep(0.08)
        ct2 = City()
        self.assertNotEqual(ct1.created_at, ct2.created_at)

    def test_two_Citys_differents_updated_at(self):
        ct1 = City()
        sleep(0.08)
        ct2 = City()
        self.assertNotEqual(ct1.updated_at, ct2.updated_at)

    def test_args_unused(self):
        ct = City(None)
        self.assertNotIn(None, ct.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dt = datetime.now()
        dt_iso = dt.isoformat()
        ct = City(id="34598765", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(ct.id, "34598765")
        self.assertEqual(ct.created_at, dt)
        self.assertEqual(ct.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)


class TestCitySave(unittest.TestCase):
    """Unittest od the save method inside the City module
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
        ct = City()
        sleep(0.04)
        old_updated_at = ct.updated_at
        ct.save()
        self.assertLess(old_updated_at, ct.updated_at)

    def test_two_save(self):
        ct = City()
        sleep(0.04)
        old_updated_at = ct.updated_at
        ct.save()
        new_updated_at = ct.updated_at
        self.assertLess(old_updated_at, new_updated_at)
        sleep(0.02)
        ct.save()
        self.assertLess(new_updated_at, ct.updated_at)

    def test_save_with_argument(self):
        ct = City()
        with self.assertRaises(TypeError):
            ct.save(None)


class TestCityToDict(unittest.TestCase):
    """This the to dict methode inside the City module
    """
    def test_to_dict_type(self):
        self.assertEqual(dict, type(City().to_dict()))

    def test_to_dict_contains_keys(self):
        ct = City()
        self.assertIn("id", ct.to_dict())
        self.assertIn("created_at", ct.to_dict())
        self.assertIn("updated_at", ct.to_dict())
        self.assertIn("__class__", ct.to_dict())

    def test_to_dict_adds_args(self):
        ct = City()
        ct.text = "Wonderfull"
        ct.my_number = 89
        self.assertEqual("Wonderfull", ct.text)
        self.assertIn("my_number", ct.to_dict())

    def test_to_dict_type_attributes(self):
        ct = City()
        p_dict = ct.to_dict()
        self.assertEqual(str, type(p_dict['id']))
        self.assertEqual(str, type(p_dict['created_at']))
        self.assertEqual(str, type(p_dict['updated_at']))

    def test_to_dict_output(self):
        d = datetime.now()
        ct = City()
        ct.id = "123456"
        ct.created_at = ct.updated_at = d
        tdict = {
            'id': '123456',
            '__class__': 'City',
            'created_at': d.isoformat(),
            'updated_at': d.isoformat(),
        }
        self.assertDictEqual(ct.to_dict(), tdict)

    def test_to_dict(self):
        ct = City()
        self.assertNotEqual(ct.to_dict(), ct.__dict__)

    def test_to_dict_with_argument(self):
        ct = City()
        with self.assertRaises(TypeError):
            ct.to_dict(None)


if __name__ == "__main__":
    unittest.main()
