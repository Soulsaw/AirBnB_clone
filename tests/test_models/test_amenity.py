#!/usr/bin/python3

"""Defines unittests for models/amenity.py
unittest classes:
    TestAmenityInstantiation
    TestAmenitySave
    TestAmenityToDict
"""

import unittest
from datetime import datetime
from time import sleep
import os
from models.amenity import Amenity
import models


class TestAmenityInstantiation(unittest.TestCase):
    """This class content the unittest of the Amenity Module
    """
    def test_instance_no_args(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_instance_in_objects(self):
        self.assertIn(Amenity(), models.storage.all().values())

    def test_public_id_str(self):
        self.assertEqual(str, type(Amenity().id))

    def test_public_created_at_datetime(self):
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_public_updated_at_dattime(self):
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_name_public_attribute(self):
        s = Amenity()
        self.assertEqual(str, type(s.id))
        self.assertIn("name", dir(s))
        self.assertNotIn("name", s.__dict__)

    def test_two_Amenitys_unique_ids(self):
        s1 = Amenity()
        s2 = Amenity()
        self.assertNotEqual(s1.id, s2.id)

    def test_two_Amenitys_differents_created_at(self):
        s1 = Amenity()
        sleep(0.08)
        s2 = Amenity()
        self.assertNotEqual(s1.created_at, s2.created_at)

    def test_two_Amenitys_differents_updated_at(self):
        s1 = Amenity()
        sleep(0.08)
        s2 = Amenity()
        self.assertNotEqual(s1.updated_at, s2.updated_at)

    def test_args_unused(self):
        s = Amenity(None)
        self.assertNotIn(None, s.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dt = datetime.now()
        dt_iso = dt.isoformat()
        s = Amenity(id="34598765", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(s.id, "34598765")
        self.assertEqual(s.created_at, dt)
        self.assertEqual(s.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)


class TestAmenitySave(unittest.TestCase):
    """Unittest od the save method inside the Amenity module
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
        s = Amenity()
        sleep(0.04)
        old_updated_at = s.updated_at
        s.save()
        self.assertLess(old_updated_at, s.updated_at)

    def test_two_save(self):
        s = Amenity()
        sleep(0.04)
        old_updated_at = s.updated_at
        s.save()
        new_updated_at = s.updated_at
        self.assertLess(old_updated_at, new_updated_at)
        sleep(0.02)
        s.save()
        self.assertLess(new_updated_at, s.updated_at)

    def test_save_with_argument(self):
        s = Amenity()
        with self.assertRaises(TypeError):
            s.save(None)


class TestAmenityToDict(unittest.TestCase):
    """This the to dict methode inside the Amenity module
    """
    def test_to_dict_type(self):
        self.assertEqual(dict, type(Amenity().to_dict()))

    def test_to_dict_contains_keys(self):
        s = Amenity()
        self.assertIn("id", s.to_dict())
        self.assertIn("created_at", s.to_dict())
        self.assertIn("updated_at", s.to_dict())
        self.assertIn("__class__", s.to_dict())

    def test_to_dict_adds_args(self):
        s = Amenity()
        s.name = "Ouagadougou"
        s.my_number = 89
        self.assertEqual("Ouagadougou", s.name)
        self.assertIn("my_number", s.to_dict())

    def test_to_dict_type_attributes(self):
        s = Amenity()
        p_dict = s.to_dict()
        self.assertEqual(str, type(p_dict['id']))
        self.assertEqual(str, type(p_dict['created_at']))
        self.assertEqual(str, type(p_dict['updated_at']))

    def test_to_dict_output(self):
        d = datetime.now()
        s = Amenity()
        s.id = "123456"
        s.created_at = s.updated_at = d
        tdict = {
            'id': '123456',
            '__class__': 'Amenity',
            'created_at': d.isoformat(),
            'updated_at': d.isoformat(),
        }
        self.assertDictEqual(s.to_dict(), tdict)

    def test_to_dict(self):
        s = Amenity()
        self.assertNotEqual(s.to_dict(), s.__dict__)

    def test_to_dict_with_argument(self):
        s = Amenity()
        with self.assertRaises(TypeError):
            s.to_dict(None)


if __name__ == "__main__":
    unittest.main()
