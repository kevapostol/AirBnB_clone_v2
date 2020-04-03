#!/usr/bin/python3
"""Database storage testing"""
import unittest
import os
import models.engine.db_storage
from models.state import State
from models import storage


@unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") != "db",
                 "Using filesystem isntead of database")
class TestDBStorage(unittest.TestCase):
    """ Tests the database storage"""
    def test_new(self):
