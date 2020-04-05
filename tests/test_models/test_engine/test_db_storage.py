#!/usr/bin/python3
"""Database storage testing"""
import unittest
import os
import pep8


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

    def test_pep8_db_FileStorage(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/file_db_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

if __name__ == "__main__":
    unittest.main()
