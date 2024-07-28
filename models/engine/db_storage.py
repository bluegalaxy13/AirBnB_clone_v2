#!/usr/bin/python3
"""
Contains the class DBStorage for interacting with the MySQL database.
"""

import models
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# Mapping class names to their corresponding model classes
classes = {
    "Amenity": Amenity,
    "City": City,
    "Place": Place,
    "Review": Review,
    "State": State,
    "User": User
}

class DBStorage:
    """Interacts with the MySQL database."""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object."""
        user = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        database = getenv('HBNB_MYSQL_DB')
        environment = getenv('HBNB_ENV')

        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(user, password, host, database)
        )

        if environment == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the current database session."""
        result = {}
        for class_name, class_obj in classes.items():
            if cls is None or cls is class_obj or cls is class_name:
                objects = self.__session.query(class_obj).all()
                for obj in objects:
                    key = f"{obj.__class__.__name__}.{obj.id}"
                    result[key] = obj
        return result

    def new(self, obj):
        """Add the object to the current database session."""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj if not None."""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Reloads data from the database."""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Call remove() method on the private session attribute."""
        if self.__session is not None:
            self.__session.remove()

    def get(self, cls, id):
        """
        Returns the object based on the class name and its ID, or
        None if not found.
        """
        if cls not in classes.values():
            return None

        all_cls = self.all(cls)
        return next((obj for obj in all_cls.values() if obj.id == id), None)

    def count(self, cls=None):
        """
        Count the number of objects in storage.
        """
        if cls is None:
            return sum(len(self.all(class_obj).values()) for class_obj in classes.values())

        return len(self.all(cls).values())
