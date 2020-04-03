#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel
from sqlalchemy import Column, Integer, String
import os
from sqlalchemy.orm import relationship

class State(BaseModel):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", backref="state", cascade="delete")

    else:
        @property
        def cities(self):
            city_LIST = []
            for obj in models.storage.all(City).values():
                city_LIST.append(obj)
            return city_LIST
