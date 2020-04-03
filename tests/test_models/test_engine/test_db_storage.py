#!/usr/bin/python3
"""Database storage testing"""
import unittest
import os
import MySQLdb
import models.engine.db_storage
from models.state import State
from models import storage


@unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") != "db",
                 "Using filesystem isntead of database")
class TestDBStorage(unittest.TestCase):
    """ Tests the database storage"""
    def setUp(self):
        self.db = MySQLdb.connect(host="localhost", port=3306,
                                  user="HBNB_MYSQL_USER",
                                  passwd="HBNB_MYSQL_PWD",
                                  db="HBNB_MYSQL_DB")
        self.cur = self.db.cursor()
        self.storage = DBStorage()
        self.storage.reload()

    def tearDown(self):
        """ close the connection"""
        self.cur.close
        self.db.close()
