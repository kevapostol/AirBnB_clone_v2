#!/usr/bin/python3
"""test for BaseModel"""
import unittest
import os
from models.base_model import BaseModel
import pep8


class TestBaseModel(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """ sets up an instance of a BaseModel """
        cls.base = BaseModel()
        cls.base.name = "Andres"
        cls.base.num = 2

    def tearDown(cls):
        """ tears down an instance of a BaseModel """
        del cls.base

    def setUp(self):
        """ attempt """
        base = BaseModel()

    def tearDown(self):
        """ teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_diff_id(self):
        """ tests to make sure both instances have different ids """
        m2 = BaseModel()
        self.assertNotEqual(self.m1.id, m2.id)

    def test_attributes(self):
        """ tests attributes and save/update times """
        self.m1.name = "Pepe"
        self.m1.my_number = 24

        self.assertTrue(self.m1.name, "Pepe")
        self.assertTrue(self.m1.my_number, 24)

        created = self.m1.created_at
        updated = self.m1.updated_at
        self.m1.save()
        created2 = self.m1.created_at
        updated2 = self.m1.updated_at

        self.assertEqual(created, created2)
        self.assertNotEqual(updated, updated2)

    def test_str(self):
        """ test to check the string representation """
        self.m1.name = "Pepe"
        string = "[{}] ({}) {}".format(self.m1.__class__.__name__,
                                       self.m1.id,
                                       self.m1.__dict__)
        self.assertEqual(str(self.m1), string)

    def test_checking_for_docstring_BaseModel(self):
        """ checking for docstrings"""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_method_BaseModel(self):
        """ checking if Basemodel have methods"""
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_init_BaseModel(self):
        """ test if the base is an type BaseModel"""
        self.assertTrue(isinstance(self.base, BaseModel))

    def test_to_dict_BaseModel(self):
        """ test if dictionary works"""
        base_dict = self.base.to_dict()
        self.assertEqual(self.base.__class__.__name__, 'BaseModel')
        self.assertIsInstance(base_dict['created_at'], str)
        self.assertIsInstance(base_dict['updated_at'], str)

if __name__ == "__main__":
    unittest.main()
