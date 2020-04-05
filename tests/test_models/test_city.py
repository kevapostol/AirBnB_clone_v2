#!/usr/bin/python3
"""test for city"""
import unittest
import os
from models.city import City
from models.base_model import BaseModel
from models.engine.db_storage import DBStorage
import pep8


class TestCity(unittest.TestCase):
    """ test for the City class"""

    @classmethod
    def setUpClass(cls):
        """ Test Setup"""
        cls.city = City()
        cls.city.name = "San Francisco"
        cls.city.state_id = "CA"

    @classmethod
    def tearDown(cls):
        """ tears down at the end of the test"""
        del cls.city

    def tearDown(self):
        """ teardown"""
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
        c2 = City()
        self.assertNotEqual(self.c1.id, c2.id)

    def test_attributes(self):
        """ tests attributes """
        self.assertTrue(hasattr(self.c1, "state_id"))
        self.assertTrue(hasattr(self.c1, "name"))
        self.assertIsInstance(self.c1.state_id, str)
        self.assertIsInstance(self.c1.name, str)

    def test_str(self):
        """ test to check the string representation """
        self.c1.name = "San Francisco"
        string = "[{}] ({}) {}".format(self.c1.__class__.__name__,
                                       self.c1.id,
                                       self.c1.__dict__)
        self.assertEqual(str(self.c1), string)

    def test_checking_for_docstring_City(self):
        """checking for docstrings"""
        self.assertIsNotNone(City.__doc__)

    def test_is_subclass_City(self):
        """ test if City is subclass of Basemodel"""
        self.assertTrue(issubclass(self.city.__class__, BaseModel), True)

    def test_attribute_types_City(self):
        """ test attribute type for City"""
        self.assertEqual(type(self.city.name), str)
        self.assertEqual(type(self.city.state_id), str)

    def test_to_dict_City(self):
        """test if dictionary works"""
        self.assertEqual('to_dict' in dir(self.city), True)

if __name__ == "__main__":
    unittest.main()
