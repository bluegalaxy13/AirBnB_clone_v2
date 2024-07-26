#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.city import City
import models
import sqlalchemy

STORAGE_TYPE = getenv("HBNB_TYPE_STORAGE")

class State(BaseModel, Base):
    """ Represents a state for MySQL table states.
    Inherits the SQLAlchemy Base and links to the MySQL table states
    
    Attributes:
        __tablename__(str): The name of the MySQL table to store States.
        name (aqlalchemy String): the name o the State.
        cities (sqlalchemy relationship): The state-City relationship.
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete-orphan")
    
    if STORAGE_TYPE != 'db':
        name = ''
        cities = []
        
        @property
        def cities(self):
            """Get a list of City instances
                with state_id equald to the current State.id
                
                This is a getter attribute for FileStorage
                Relationship between State and City.
            """
            city_list = []
            for city in models.storage.all(City):
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
