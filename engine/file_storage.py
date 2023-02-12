#!/usr/bin/python3
""" This module creates a class `FileStorage` """
import json
from models.base_model import BaseModel


class FileStorage:
    """ serializes instances to a JSON file and
        deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """  returns the dictionary `__objects` """

        return self.__objects

    def new(self, obj):
        """ sets in `__objects` the `obj` with key `<obj class name>.id` """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """ serializes `__objects` to the JSON file """
        with open(self.__file_path, "w", encoding="utf-8") as f:
            d = {k: v.to_dict() for k, v in self.__objects.items()}
            json.dump(d, f)

    def reload(self):
        """ Reloads the stored objects """
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                _dict = json.load(f)
                for obj_dict in _dict.values():
                    cls_name = obj_dict["__class__"]
                    del obj_dict["__class__"]
                    self.new(eval(cls_name)(**obj_dict))
        except FileNotFoundError:
            return
