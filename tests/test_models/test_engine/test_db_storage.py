#!/usr/bin/python3
"""Database storage testing"""
import unittest
import os
import pep8
import MySQLdb
from models.engine.db_storage import DBStorage
from models.state import State


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

    def test_pep8_db_FileStorage(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/file_db_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

         @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', 'db')

    def test_add(self):
        """Test add method"""
        self.cur.execute("""
        INSERT INTO states (id, created_at, updated_at, name)
        VALUES (1, '2017-11-10 00:30:12', '2017-11-10 00:30:12', "California")
        """)
        self.cur.execute('SELECT * FROM states')
        rows = self.cur.fetchall()
        self.assertEqual(len(rows), 1)


if __name__ == "__main__":
    unittest.main()
