#!/usr/bin/python3
"""test for user"""
import unittest
import os
from models.user import User
from models.base_model import BaseModel
import pep8


class TestUser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """ test set up"""
        cls.user = User()
        cls.user.first_name = "Brad"
        cls.user.last_name = "Goldilocks"
        cls.user.email = "erika.caoili@gmail.com"
        cls.user.password = "qttt3"

    @classmethod
    def tearDown(cls):
        """ tears down at the end of the test"""
        del cls.user

    def tearDown(self):
        """ teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_diff_id(self):
        """ tests to make sure both instances have different ids """
        u2 = User()
        self.assertNotEqual(self.u1.id, u2.id)

    def test_attributes(self):
        """ tests attributes to make sure they are string """
        self.assertIsInstance(self.u1.email, str)
        self.assertIsInstance(self.u1.password, str)
        self.assertIsInstance(self.u1.first_name, str)
        self.assertIsInstance(self.u1.last_name, str)

    def test_str(self):
        """ test to check the string representation """
        self.u1.first_name = "Pepe"
        string = "[{}] ({}) {}".format(self.u1.__class__.__name__,
                                       self.u1.id,
                                       self.u1.__dict__)
        self.assertEqual(str(self.u1), string)

    def test_checking_for_docstring_User(self):
        """ checking for docstrings"""
        self.assertIsNotNone(User.__doc__)

    def test_is_subclass_User(self):
        """ test if User is subclass of Basemodel"""
        self.assertTrue(issubclass(self.user.__class__, BaseModel), True)

    def test_to_dict_User(self):
        """ test if dictionary works"""
        self.assertEqual('to_dict' in dir(self.user), True)

                     "Incorrect storage type")

if __name__ == "__main__":
    unittest.main()
