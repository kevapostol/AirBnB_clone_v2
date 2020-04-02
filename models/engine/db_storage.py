#!/usr/bin/python3
"""db_stroage module"""
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models.base_model import Base
from sqlalchemy.orm import scoped_session
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import os


class DBStorage:
    """DBStorage class
    """

    __engine = None
    __session = None

    def __init__(self):
        """Init function
        """
        user = os.getenv("HBNB_MYSQL_USER")
        pw = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        dbase = os.getenv("HBNB_MYSQL_DB")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            user, pw, host, dbase), pool_pre_ping=True)

        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Runs session queries and returns a dictionary
        """
        my_dict = {}
        t = []
        new_t = []
        if cls is not None:
            t = session.query(cls).all()
        else:
            class_list = [User, State, City, Amenity, Place, Review]

            for cls_name in class_list:
                t.append(session.query(cls_name).all())

            for y in t:
                for x in y:
                    new_t.append(x)
            t = new_t[:]

        for obj in t:
            my_dict['{}.{}'.format(obj.__class__.__name__, obj.id)] = obj

        return my_dict

    def new(self, obj):
        """
        Add object to current db
        """
        self.__session.add(obj)

    def save(self):
        """
        Commit object to current db
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Delete object to current db
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
        Reload objects to current db
        """
        Base.metadata.create_all(self.__engine)
        session_fact = sessionmaker(bind=self.__engine)
        Session = scoped_session(session_fact)
        self.__session = Session(expire_on_commit=False)

    def close(self):
        """Closes the session
        """
        self.__session.close()
