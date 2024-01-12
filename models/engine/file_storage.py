"""Defining the file storage module"""
import json
import os
from models.base_model import BaseModel


class Filestorage:
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
        Filestorage.__objects[key] = obj

    def all(self):
        """To display the __objects"""

        return Filestorage.__objects

    def save(self):
        """To serialize __object dictionary to JSON file"""

        all_objs = Filestorage.__objects
        object_dict = {}
        for i in all_objs.keys():
            object_dict[i] = all_objs[i].to_dict()
        with open(Filestorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(object_dict, f)

    def reload(self):
        """To deserialize from JSON file to __object"""

        if os.path.isfile(Filestorage.__file_path):
            with open(Filestorage.__file_path, "r", encoding="utf-8") as f:
                try:
                    object_dict = json.load(f)

                    for key, value in object_dict.items():
                        class_name, obj_id = key.split(".")
                        cls = eval(class_name)
                        instance = cls(**value)
                        Filestorage.__objects[key] = instance
                except Exception:
                    pass
