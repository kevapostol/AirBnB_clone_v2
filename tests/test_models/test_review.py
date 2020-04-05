#!/usr/bin/python3
"""test for review"""
import unittest
import os
from models.review import Review
from models.base_model import BaseModel
import pep8


class TestReview(unittest.TestCase):

    @classmethod
    def setUp(cls):
        """ sets up test"""
        cls.review = Review()
        cls.review.place_id = "0246-kdks"
        cls.review.user_id = "6420-kds"
        cls.review.text = "Cutest cottage in the world"

    @classmethod
    def tearDown(cls):
        """ tears down at the end of the test"""
        del cls.review

    def tearDown(self):
        """teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8(self):
        """ tests files to pep8 standard"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_diff_id(self):
        """ tests to make sure both instances have different ids"""
        r2 = Review()
        self.assertNotEqual(self.r1.id, r2.id)

    def test_attributes(self):
        """ tests attributes"""
        self.assertTrue(hasattr(self.r1, "place_id"))
        self.assertTrue(hasattr(self.r1, "user_id"))
        self.assertTrue(hasattr(self.r1, "text"))
        self.assertIsInstance(self.r1.place_id, str)
        self.assertIsInstance(self.r1.user_id, str)
        self.assertIsInstance(self.r1.text, str)

    def test_str(self):
        """ test to check the string representation"""
        self.r1.name = "5 Stars"
        string = "[{}] ({}) {}".format(self.r1.__class__.__name__,
                                       self.r1.id,
                                       self.r1.__dict__)
        self.assertEqual(str(self.r1), string)

    def test_checking_for_docstring_Review(self):
        """ checking for docstrings"""
        self.assertIsNotNone(Review.__doc__)

    def test_is_subclass_Review(self):
        """ test if review is subclass of BaseModel"""
        self.assertTrue(issubclass(self.rev.__class__, BaseModel), True)

    def test_to_dict_Review(self):
        """test if dictionary works"""
        self.assertEqual('to_dict' in dir(self.rev), True)

if __name__ == "__main__":
    unittest.main()
