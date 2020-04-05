#!/usr/bin/python3
"""test for state"""
import unittest
import os
from models.state import State
from models.base_model import BaseModel
import pep8


class TestState(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """ test set up"""
        cls.state = State()
        cls.state.name = "NC"

    @classmethod
    def tearDown(self):
        """ tears down at the end of test"""
        del cls.state

    def tearDown(self):
        """teardown"""
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
        s2 = State()
        self.assertNotEqual(self.s1.id, s2.id)

    def test_attributes(self):
        """ tests attributes and save/update times """
        self.s1.name = "California"
        self.assertTrue(hasattr(self.s1, "name"))
        self.assertIsInstance(self.s1.name, str)

        created = self.s1.created_at
        updated = self.s1.updated_at
        self.s1.save()
        created2 = self.s1.created_at
        updated2 = self.s1.updated_at

        self.assertEqual(created, created2)
        self.assertNotEqual(updated, updated2)

    def test_str(self):
        """ test to check the string representation """
        self.s1.name = "California"
        string = "[{}] ({}) {}".format(self.s1.__class__.__name__,
                                       self.s1.id,
                                       self.s1.__dict__)
        self.assertEqual(str(self.s1), string)

    def test_checking_for_docstring_State(self):
        """ checking for docstrings"""
        self.assertIsNotNone(State.__doc__)

    def test_is_subclass_State(self):
        """ test if State is subclass of BaseModel"""
        self.assertTrue(issubclass(self.state.__class__, BaseModel), True)

    def test_to_dict_State(self):
        """ test if dictionary works"""
        self.assertEqual('to_dict' in dir(self.state), True)

if __name__ == "__main__":
    unittest.main()
