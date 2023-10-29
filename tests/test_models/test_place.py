#!/usr/bin/python3

"""Defines unittests for models/place.py
unittest classes:
    TestPlaceInstantiation
    TestPlaceSave
    TestPlaceToDict
"""
import unittest
from datetime import datetime
from time import sleep
import os
from models.place import Place
import models


class TestPlaceInstantiation(unittest.TestCase):
    """This class content the unittest of the Place Module
    """
    def test_instance_no_args(self):
        self.assertEqual(Place, type(Place()))

    def test_instance_in_objects(self):
        self.assertIn(Place(), models.storage.all().values())

    def test_public_id_str(self):
        self.assertEqual(str, type(Place().id))

    def test_public_created_at_datetime(self):
        self.assertEqual(datetime, type(Place().created_at))

    def test_public_updated_at_dattime(self):
        self.assertEqual(datetime, type(Place().updated_at))

    def test_city_id_is_public_attribute(self):
        p = Place()
        self.assertEqual(str, type(p.id))
        self.assertIn("city_id", dir(p))
        self.assertNotIn("city_id", p.__dict__)

    def test_user_id_is_public_attribute(self):
        pu = Place()
        self.assertEqual(str, type(pu.id))
        self.assertIn("user_id", dir(pu))
        self.assertNotIn("user_id", pu.__dict__)

    def test_name_is_public_attribute(self):
        pn = Place()
        self.assertEqual(str, type(pn.id))
        self.assertIn("name", dir(pn))
        self.assertNotIn("name", pn.__dict__)

    def test_description_is_public_attribute(self):
        pd = Place()
        self.assertEqual(str, type(pd.id))
        self.assertIn("description", dir(pd))
        self.assertNotIn("description", pd.__dict__)

    def test_number_rooms_is_public_attribute(self):
        pnr = Place()
        self.assertEqual(str, type(pnr.id))
        self.assertIn("number_rooms", dir(pnr))
        self.assertNotIn("number_rooms", pnr.__dict__)

    def test_number_bathrooms_is_public_attribute(self):
        pnb = Place()
        self.assertEqual(str, type(pnb.id))
        self.assertIn("number_bathrooms", dir(pnb))
        self.assertNotIn("number_bathrooms", pnb.__dict__)

    def test_max_guest_is_public_instance(self):
        p = Place()
        self.assertEqual(str, type(p.id))
        self.assertIn("max_guest", dir(p))
        self.assertNotIn("max_guest", p.__dict__)

    def test_price_by_night_is_public_instance(self):
        p = Place()
        self.assertEqual(str, type(p.id))
        self.assertIn("price_by_night", dir(p))
        self.assertNotIn("price_by_night", p.__dict__)

    def test_latitude_is_public_instance(self):
        p = Place()
        self.assertEqual(str, type(p.id))
        self.assertIn("latitude", dir(p))
        self.assertNotIn("latitude", p.__dict__)

    def test_longitude_is_public_instance(self):
        p = Place()
        self.assertEqual(str, type(p.id))
        self.assertIn("longitude", dir(p))
        self.assertNotIn("longitude", p.__dict__)

    def test_amenity_ids_is_public_instance(self):
        p = Place()
        self.assertEqual(str, type(p.id))
        self.assertIn("amenity_ids", dir(p))
        self.assertNotIn("amenity_ids", p.__dict__)

    def test_two_places_unique_ids(self):
        p1 = Place()
        p2 = Place()
        self.assertNotEqual(p1.id, p2.id)

    def test_two_places_differents_created_at(self):
        p1 = Place()
        sleep(0.08)
        p2 = Place()
        self.assertNotEqual(p1.created_at, p2.created_at)

    def test_two_places_differents_updated_at(self):
        p1 = Place()
        sleep(0.08)
        p2 = Place()
        self.assertNotEqual(p1.updated_at, p2.updated_at)

    def test_args_unused(self):
        p = Place(None)
        self.assertNotIn(None, p.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dt = datetime.now()
        dt_iso = dt.isoformat()
        p = Place(id="34598765", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(p.id, "34598765")
        self.assertEqual(p.created_at, dt)
        self.assertEqual(p.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Place(id=None, created_at=None, updated_at=None)


class TestPlaceSave(unittest.TestCase):
    """Unittest od the save method inside the Place module
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
        p = Place()
        sleep(0.04)
        old_updated_at = p.updated_at
        p.save()
        self.assertLess(old_updated_at, p.updated_at)

    def test_two_save(self):
        p = Place()
        sleep(0.04)
        old_updated_at = p.updated_at
        p.save()
        new_updated_at = p.updated_at
        self.assertLess(old_updated_at, new_updated_at)
        sleep(0.02)
        p.save()
        self.assertLess(new_updated_at, p.updated_at)

    def test_save_with_argument(self):
        p = Place()
        with self.assertRaises(TypeError):
            p.save(None)


class TestPlaceToDict(unittest.TestCase):
    """This the to dict methode inside the Place module
    """
    def test_to_dict_type(self):
        self.assertEqual(dict, type(Place().to_dict()))

    def test_to_dict_contains_keys(self):
        p = Place()
        self.assertIn("id", p.to_dict())
        self.assertIn("created_at", p.to_dict())
        self.assertIn("updated_at", p.to_dict())
        self.assertIn("__class__", p.to_dict())

    def test_to_dict_adds_args(self):
        p = Place()
        p.first_name = "Betty"
        p.my_number = 456
        self.assertEqual("Betty", p.first_name)
        self.assertIn("my_number", p.to_dict())

    def test_to_dict_type_attributes(self):
        p = Place()
        p_dict = p.to_dict()
        self.assertEqual(str, type(p_dict['id']))
        self.assertEqual(str, type(p_dict['created_at']))
        self.assertEqual(str, type(p_dict['updated_at']))

    def test_to_dict_output(self):
        d = datetime.now()
        p = Place()
        p.id = "123456"
        p.created_at = p.updated_at = d
        tdict = {
            'id': '123456',
            '__class__': 'Place',
            'created_at': d.isoformat(),
            'updated_at': d.isoformat(),
        }
        self.assertDictEqual(p.to_dict(), tdict)

    def test_to_dict(self):
        p = Place()
        self.assertNotEqual(p.to_dict(), p.__dict__)

    def test_to_dict_with_argument(self):
        p = Place()
        with self.assertRaises(TypeError):
            p.to_dict(None)


if __name__ == "__main__":
    unittest.main()
