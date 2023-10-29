#!/usr/bin/python3

"""Defines unittests for models/user.py
unittest classes:
    TestUserInstantiation
    TestUserSave
    TestUserToDict
"""

import unittest
from datetime import datetime
from time import sleep
import os
from models.user import User
import models


class TestUserInstantiation(unittest.TestCase):
    """This class content the unittest of the User Module
    """
    def test_instance_no_args(self):
        self.assertEqual(User, type(User()))

    def test_instance_in_objects(self):
        self.assertIn(User(), models.storage.all().values())

    def test_public_id_str(self):
        self.assertEqual(str, type(User().id))

    def test_public_created_at_datetime(self):
        self.assertEqual(datetime, type(User().created_at))

    def test_public_updated_at_dattime(self):
        self.assertEqual(datetime, type(User().updated_at))

    def test_email_is_public_attribute(self):
        p = User()
        self.assertEqual(str, type(p.id))
        self.assertIn("email", dir(p))
        self.assertNotIn("email", p.__dict__)

    def test_password_is_public_attribute(self):
        pu = User()
        self.assertEqual(str, type(pu.id))
        self.assertIn("password", dir(pu))
        self.assertNotIn("password", pu.__dict__)

    def test_first_name_is_public_attribute(self):
        pn = User()
        self.assertEqual(str, type(pn.id))
        self.assertIn("first_name", dir(pn))
        self.assertNotIn("first_name", pn.__dict__)

    def test_last_name_is_public_attribute(self):
        pd = User()
        self.assertEqual(str, type(pd.id))
        self.assertIn("last_name", dir(pd))
        self.assertNotIn("last_name", pd.__dict__)

    def test_two_Users_unique_ids(self):
        p1 = User()
        p2 = User()
        self.assertNotEqual(p1.id, p2.id)

    def test_two_Users_differents_created_at(self):
        p1 = User()
        sleep(0.08)
        p2 = User()
        self.assertNotEqual(p1.created_at, p2.created_at)

    def test_two_Users_differents_updated_at(self):
        p1 = User()
        sleep(0.08)
        p2 = User()
        self.assertNotEqual(p1.updated_at, p2.updated_at)

    def test_args_unused(self):
        p = User(None)
        self.assertNotIn(None, p.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dt = datetime.now()
        dt_iso = dt.isoformat()
        p = User(id="34598765", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(p.id, "34598765")
        self.assertEqual(p.created_at, dt)
        self.assertEqual(p.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            User(id=None, created_at=None, updated_at=None)


class TestUserSave(unittest.TestCase):
    """Unittest od the save method inside the User module
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
        p = User()
        sleep(0.04)
        old_updated_at = p.updated_at
        p.save()
        self.assertLess(old_updated_at, p.updated_at)

    def test_two_save(self):
        p = User()
        sleep(0.04)
        old_updated_at = p.updated_at
        p.save()
        new_updated_at = p.updated_at
        self.assertLess(old_updated_at, new_updated_at)
        sleep(0.02)
        p.save()
        self.assertLess(new_updated_at, p.updated_at)

    def test_save_with_argument(self):
        p = User()
        with self.assertRaises(TypeError):
            p.save(None)


class TestUserToDict(unittest.TestCase):
    """This the to dict methode inside the User module
    """
    def test_to_dict_type(self):
        self.assertEqual(dict, type(User().to_dict()))

    def test_to_dict_contains_keys(self):
        p = User()
        self.assertIn("id", p.to_dict())
        self.assertIn("created_at", p.to_dict())
        self.assertIn("updated_at", p.to_dict())
        self.assertIn("__class__", p.to_dict())

    def test_to_dict_adds_args(self):
        p = User()
        p.first_name = "Betty"
        p.my_number = 456
        self.assertEqual("Betty", p.first_name)
        self.assertIn("my_number", p.to_dict())

    def test_to_dict_type_attributes(self):
        p = User()
        p_dict = p.to_dict()
        self.assertEqual(str, type(p_dict['id']))
        self.assertEqual(str, type(p_dict['created_at']))
        self.assertEqual(str, type(p_dict['updated_at']))

    def test_to_dict_output(self):
        d = datetime.now()
        p = User()
        p.id = "123456"
        p.created_at = p.updated_at = d
        tdict = {
            'id': '123456',
            '__class__': 'User',
            'created_at': d.isoformat(),
            'updated_at': d.isoformat(),
        }
        self.assertDictEqual(p.to_dict(), tdict)

    def test_to_dict(self):
        p = User()
        self.assertNotEqual(p.to_dict(), p.__dict__)

    def test_to_dict_with_argument(self):
        p = User()
        with self.assertRaises(TypeError):
            p.to_dict(None)


if __name__ == "__main__":
    unittest.main()
