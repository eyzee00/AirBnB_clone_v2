#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String 
from sqlalchemy.orm import relationship
import models
from models.city import City

class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="delete")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """Gets a list of all related City objects"""
            city_list = []
            city_dictionary = models.storage.all(City)
            for city in list(city_dictionary.values()):
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
