#!/usr/bin/python3

"""Defines unittests for models/State.py
unittest classes:
    TestStateInstantiation
    TestStateSave
    TestStateToDict
"""
import unittest
from datetime import datetime
from time import sleep
import os
from models.state import State
import models


class TestStateInstantiation(unittest.TestCase):
    """This class content the unittest of the State Module
    """
    def test_instance_no_args(self):
        self.assertEqual(State, type(State()))

    def test_instance_in_objects(self):
        self.assertIn(State(), models.storage.all().values())

    def test_public_id_str(self):
        self.assertEqual(str, type(State().id))

    def test_public_created_at_datetime(self):
        self.assertEqual(datetime, type(State().created_at))

    def test_public_updated_at_dattime(self):
        self.assertEqual(datetime, type(State().updated_at))

    def test_name_public_attribute(self):
        s = State()
        self.assertEqual(str, type(s.id))
        self.assertIn("name", dir(s))
        self.assertNotIn("name", s.__dict__)

    def test_two_States_unique_ids(self):
        s1 = State()
        s2 = State()
        self.assertNotEqual(s1.id, s2.id)

    def test_two_States_differents_created_at(self):
        s1 = State()
        sleep(0.08)
        s2 = State()
        self.assertNotEqual(s1.created_at, s2.created_at)

    def test_two_States_differents_updated_at(self):
        s1 = State()
        sleep(0.08)
        s2 = State()
        self.assertNotEqual(s1.updated_at, s2.updated_at)

    def test_args_unused(self):
        s = State(None)
        self.assertNotIn(None, s.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dt = datetime.now()
        dt_iso = dt.isoformat()
        s = State(id="34598765", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(s.id, "34598765")
        self.assertEqual(s.created_at, dt)
        self.assertEqual(s.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            State(id=None, created_at=None, updated_at=None)


class TestStateSave(unittest.TestCase):
    """Unittest od the save method inside the State module
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
        s = State()
        sleep(0.04)
        old_updated_at = s.updated_at
        s.save()
        self.assertLess(old_updated_at, s.updated_at)

    def test_two_save(self):
        s = State()
        sleep(0.04)
        old_updated_at = s.updated_at
        s.save()
        new_updated_at = s.updated_at
        self.assertLess(old_updated_at, new_updated_at)
        sleep(0.02)
        s.save()
        self.assertLess(new_updated_at, s.updated_at)

    def test_save_with_argument(self):
        s = State()
        with self.assertRaises(TypeError):
            s.save(None)


class TestStateToDict(unittest.TestCase):
    """This the to dict methode inside the State module
    """
    def test_to_dict_type(self):
        self.assertEqual(dict, type(State().to_dict()))

    def test_to_dict_contains_keys(self):
        s = State()
        self.assertIn("id", s.to_dict())
        self.assertIn("created_at", s.to_dict())
        self.assertIn("updated_at", s.to_dict())
        self.assertIn("__class__", s.to_dict())

    def test_to_dict_adds_args(self):
        s = State()
        s.name = "Ouagadougou"
        s.my_number = 89
        self.assertEqual("Ouagadougou", s.name)
        self.assertIn("my_number", s.to_dict())

    def test_to_dict_type_attributes(self):
        s = State()
        p_dict = s.to_dict()
        self.assertEqual(str, type(p_dict['id']))
        self.assertEqual(str, type(p_dict['created_at']))
        self.assertEqual(str, type(p_dict['updated_at']))

    def test_to_dict_output(self):
        d = datetime.now()
        s = State()
        s.id = "123456"
        s.created_at = s.updated_at = d
        tdict = {
            'id': '123456',
            '__class__': 'State',
            'created_at': d.isoformat(),
            'updated_at': d.isoformat(),
        }
        self.assertDictEqual(s.to_dict(), tdict)

    def test_to_dict(self):
        s = State()
        self.assertNotEqual(s.to_dict(), s.__dict__)

    def test_to_dict_with_argument(self):
        s = State()
        with self.assertRaises(TypeError):
            s.to_dict(None)


if __name__ == "__main__":
    unittest.main()
