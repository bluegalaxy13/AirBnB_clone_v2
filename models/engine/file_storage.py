#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage.

        Args:
            cls (class, optional): If specified, filters the result to include
                only objects of the specified class.

        Returns:
            dict: A dictionary containing objects in storage.
        """
        if cls is not None:
            if isinstance(cls, str):
                try:
                    cls = globals()[cls]
                    print(cls)
                except Exception as e:
                    print('cls not valid: ', e)
            cls_dict = {}
            for k, v in self.__objects.items():
                if cls == type(v):
                    cls_dict[k] = v
            return cls_dict
        return self.__objects
                

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        """Saves storage dictionary to file"""
        odict = {o: self.__object[o].to_dict() for o in self.__objects.keys()}
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(odict, f)

    def reload(self):
        """Loads storage dictionary from file."""
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                for o in json.load(f).values():
                    name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(name)(**o))
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """
         Delete obj from __objects if it’s inside - if obj is equal to None,
           the method should not do anything
        """
        try:
            del self.__objects["{}.{}".format(type(obj).__name__, obj.id)]
        except (AttributeError, KeyError):
            pass
        
    def close(self):
        """Call the reload method."""
        self.reload()
