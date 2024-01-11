#!/usr/bin/python3
'''Defining the BaseModel Class'''
from datetime import datetime
import uuid

class BaseModel:
    """This represents the BaseModel of thie HBnb project"""

    def __init__(self):
        """The constructor"""

        self.id = str(uuid.uuid4())

        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def save(self):
        """Updates the public instance attribute updated_at
        with the current time"""
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """It returns a dictionary containing all keys and values of dict"""
        dict_inst = self.__dict__.copy()

        dict_inst["__class__"] = self.__class__.__name__
        dict_inst["created_at"] = self.created_at.isoformat()
        dict_inst["updated_at"] = self.updated_at.isoformat()

        return dict_inst
    
    def __str__(self):
        """Returns the str representation of
        BaseModel  instance"""

        cl_name = self.__class__.__name__
        return "[{}] ({}) {}".format(cl_name, self.id, self.__dict__)
