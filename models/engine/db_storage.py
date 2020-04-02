#!/usr/bin/python3
"""db_stroage module"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """DBStorage class
    """

    __engine = None
    __session = None
    cls_names = [User, State, City, Amenity, Place, Review]

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
        """query all objs"""
        t_dict = {}
        if cls is None:
            for typ in self.cls_names:
                for obj in self.__session.query(typ).all():
                    key = "{}.{}".format(obj.__class__.__name__, obj.id)
                    t_dict[key] = obj
        else:
            for obj in self.__session.query(cls).all():
                key = "{}.{}".format(cls.__class__.__name__, obj.id)
                t_dict[key] = obj
        return t_dict

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
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)

    def close(self):
        """Closes the session
        """
        if self.__session:
            self.__session.remove()
