#!/usr/bin/python3
"""test for place"""
import unittest
import os
from models.place import Place
from models.base_model import BaseModel
import pep8


class TestPlace(unittest.TestCase):

    @classmethod
    def setUp(cls):
        """ Set up for tests"""
        cls.place = Place()
        cls.place.user_id = "0123-abcd"
        cls.place.city_id = "3210-dcba"
        cls.place.name = "Hexagon House"
        cls.place.description = "A cute cottage by the sea"
        cls.place.number_rooms = 3
        cls.place.number_bathrooms = 2
        cls.place.max_guest = 200
        cls.place.price_by_night = 100
        cls.place.latitude = 37.7749
        cls.place.longitude = 122.4194
        cls.place.amenity_ids = ["2468-fghijkl"]

    @classmethod
    def teardown(cls):
        """ tears it down"""
        del cls.place

    def tearDown(self):
        """ tears down an instance of a Place """
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8(self):
        """ tests files to pep8 standard """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_diff_id(self):
        """ tests to make sure both instances have different ids """
        p2 = Place()
        self.assertNotEqual(self.p1.id, p2.id)

    def test_attributes(self):
        """ tests attributes to make sure they are strings/integers/floats """
        self.assertIsInstance(self.p1.city_id, str)
        self.assertIsInstance(self.p1.user_id, str)
        self.assertIsInstance(self.p1.name, str)
        self.assertIsInstance(self.p1.description, str)
        self.assertIsInstance(self.p1.number_rooms, int)
        self.assertIsInstance(self.p1.number_bathrooms, int)
        self.assertIsInstance(self.p1.max_guest, int)
        self.assertIsInstance(self.p1.price_by_night, int)
        self.assertIsInstance(self.p1.latitude, float)
        self.assertIsInstance(self.p1.longitude, float)
        """self.assertIsInstance(self.p1.amenity_ids, int)"""

    def test_has_attr(self):
        """ test to make sure class has attributes """
        self.assertTrue(hasattr(self.p1, "city_id"))
        self.assertTrue(hasattr(self.p1, "user_id"))
        self.assertTrue(hasattr(self.p1, "name"))
        self.assertTrue(hasattr(self.p1, "description"))
        self.assertTrue(hasattr(self.p1, "number_rooms"))
        self.assertTrue(hasattr(self.p1, "number_bathrooms"))
        self.assertTrue(hasattr(self.p1, "max_guest"))
        self.assertTrue(hasattr(self.p1, "price_by_night"))
        self.assertTrue(hasattr(self.p1, "latitude"))
        self.assertTrue(hasattr(self.p1, "longitude"))
        self.assertTrue(hasattr(self.p1, "amenity_ids"))

    def test_str(self):
        """ test to check the string representation """
        self.p1.name = "US"
        string = "[{}] ({}) {}".format(self.p1.__class__.__name__,
                                       self.p1.id,
                                       self.p1.__dict__)
        self.assertEqual(str(self.p1), string)

    def test_to_dict_Place(self):
        """test if dictionary works"""
        self.assertEqual('to_dict' in dir(self.place), True)

if __name__ == "__main__":
    unittest.main()
