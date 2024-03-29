#!/usr/bin/python3
"""Defining the file storage module"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Represent an abstract storage engine
    __file_path: The name of file to save objects to
    __objects: A dictionary of object
    """
    __file_path = "file.json"
    __objects = {}

    def new(self, obj):
        """set the __object to <class_name>.id"""

        obj_class_name = obj.__class__.__name__
        key = "{}.{}".format(obj_class_name, obj.id)
        FileStorage.__objects[key] = obj

    def all(self):
        """To display the __objects"""

        return FileStorage.__objects

    def save(self):
        """To serialize __object dictionary to JSON file"""

        all_objs = FileStorage.__objects
        object_dict = {}
        for i in all_objs.keys():
            object_dict[i] = all_objs[i].to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(object_dict, f)

    def reload(self):
        """To deserialize from JSON file to __object"""

        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                try:
                    object_dict = json.load(f)

                    for key, value in object_dict.items():
                        class_name, obj_id = key.split(".")
                        cls = eval(class_name)
                        instance = cls(**value)
                        FileStorage.__objects[key] = instance
                except Exception:
                    pass
