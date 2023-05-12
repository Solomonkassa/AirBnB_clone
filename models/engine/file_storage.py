#!/usr/bin/python3
'''Defines the FileStorage class. '''

import json
from models.base_model import BaseModel
from os import path


class FileStorage:
    """
    File Storage Class
   
    """
    __file_path = 'objects.json'
    __objects = {}

    def all(self):
        """
        Returns the content of the `__objects` class attribute.
        """
        return self.__objects

    def new(self, obj):
        """
        Saves a new object in the `__objects` class attribute
       
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serializes the content of `__objects` 
        """
        json_dict = {}
        for key, value in self.__objects.items():
            json_dict[key] = value.to_dict()
        with open(self.__file_path, mode='w', encoding='utf-8') as f:
            f.write(json.dumps(json_dict))

    def reload(self):
        """
        Deserializes the JSON file in `__file_path` 
        """
        if path.exists(self.__file_path):
            with open(self.__file_path, mode='r', encoding='utf-8') as f:
                json_dict = json.loads(f.read())
                for key, value in json_dict.items():
                    self.__objects[key] = eval(value['__class__'])(**value)
