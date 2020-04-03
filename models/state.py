#!/usr/bin/python3
"""This is the state class"""
import os
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """

    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="all, delete")

    @property
    def cities(self):
        city_list = []
        for obj in models.storage.all(City).items():
            if obj.state_id == self.id:
                city_list.append(obj)
        return city_list
