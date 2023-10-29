#!/usr/bin/python3

"""Defines unittests for models/Review.py
unittest classes:
    TestReviewInstantiation
    TestReviewSave
    TestReviewToDict
"""
import unittest
from datetime import datetime
from time import sleep
import os
from models.review import Review
import models


class TestReviewInstantiation(unittest.TestCase):
    """This class content the unittest of the Review Module
    """
    def test_instance_no_args(self):
        self.assertEqual(Review, type(Review()))

    def test_instance_in_objects(self):
        self.assertIn(Review(), models.storage.all().values())

    def test_public_id_str(self):
        self.assertEqual(str, type(Review().id))

    def test_public_created_at_datetime(self):
        self.assertEqual(datetime, type(Review().created_at))

    def test_public_updated_at_dattime(self):
        self.assertEqual(datetime, type(Review().updated_at))

    def test_place_id_is_public_attribute(self):
        rp = Review()
        self.assertEqual(str, type(rp.id))
        self.assertIn("place_id", dir(rp))
        self.assertNotIn("place_id", rp.__dict__)

    def test_user_id_is_public_attribute(self):
        ru = Review()
        self.assertEqual(str, type(ru.id))
        self.assertIn("user_id", dir(ru))
        self.assertNotIn("user_id", ru.__dict__)

    def test_text_is_public_attribute(self):
        rt = Review()
        self.assertEqual(str, type(rt.id))
        self.assertIn("text", dir(rt))
        self.assertNotIn("text", rt.__dict__)

    def test_two_Reviews_unique_ids(self):
        r1 = Review()
        r2 = Review()
        self.assertNotEqual(r1.id, r2.id)

    def test_two_Reviews_differents_created_at(self):
        r1 = Review()
        sleep(0.08)
        r2 = Review()
        self.assertNotEqual(r1.created_at, r2.created_at)

    def test_two_Reviews_differents_updated_at(self):
        r1 = Review()
        sleep(0.08)
        r2 = Review()
        self.assertNotEqual(r1.updated_at, r2.updated_at)

    def test_args_unused(self):
        r = Review(None)
        self.assertNotIn(None, r.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dt = datetime.now()
        dt_iso = dt.isoformat()
        r = Review(id="34598765", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(r.id, "34598765")
        self.assertEqual(r.created_at, dt)
        self.assertEqual(r.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Review(id=None, created_at=None, updated_at=None)


class TestReviewSave(unittest.TestCase):
    """Unittest od the save method inside the Review module
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
        r = Review()
        sleep(0.04)
        old_updated_at = r.updated_at
        r.save()
        self.assertLess(old_updated_at, r.updated_at)

    def test_two_save(self):
        r = Review()
        sleep(0.04)
        old_updated_at = r.updated_at
        r.save()
        new_updated_at = r.updated_at
        self.assertLess(old_updated_at, new_updated_at)
        sleep(0.02)
        r.save()
        self.assertLess(new_updated_at, r.updated_at)

    def test_save_with_argument(self):
        r = Review()
        with self.assertRaises(TypeError):
            r.save(None)


class TestReviewToDict(unittest.TestCase):
    """This the to dict methode inside the Review module
    """
    def test_to_dict_type(self):
        self.assertEqual(dict, type(Review().to_dict()))

    def test_to_dict_contains_keys(self):
        r = Review()
        self.assertIn("id", r.to_dict())
        self.assertIn("created_at", r.to_dict())
        self.assertIn("updated_at", r.to_dict())
        self.assertIn("__class__", r.to_dict())

    def test_to_dict_adds_args(self):
        r = Review()
        r.text = "Wonderfull"
        r.my_number = 89
        self.assertEqual("Wonderfull", r.text)
        self.assertIn("my_number", r.to_dict())

    def test_to_dict_type_attributes(self):
        r = Review()
        p_dict = r.to_dict()
        self.assertEqual(str, type(p_dict['id']))
        self.assertEqual(str, type(p_dict['created_at']))
        self.assertEqual(str, type(p_dict['updated_at']))

    def test_to_dict_output(self):
        d = datetime.now()
        r = Review()
        r.id = "123456"
        r.created_at = r.updated_at = d
        tdict = {
            'id': '123456',
            '__class__': 'Review',
            'created_at': d.isoformat(),
            'updated_at': d.isoformat(),
        }
        self.assertDictEqual(r.to_dict(), tdict)

    def test_to_dict(self):
        r = Review()
        self.assertNotEqual(r.to_dict(), r.__dict__)

    def test_to_dict_with_argument(self):
        r = Review()
        with self.assertRaises(TypeError):
            r.to_dict(None)


if __name__ == "__main__":
    unittest.main()
