#!/usr/bin/python3
import json
import os
"""a model that will contain the class FileStorage"""


class FileStorage:
    """a class that will take care of serialization and desrialization"""
    __file_path = "first.json"
    __objects = {}

    def all(self):
        """returns the dictionary objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + str(obj.id)
        self.__objects[key] = obj

    def to_dictionary(self, obj):
        """
        convert an obj to a dictionary so that way it can be serailizable
        """
        return obj.__dict__
    
    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        dictionary_of_dicts = {}
        for key, value in self.__objects.items():
            dictionary_of_dicts[key] = self.to_dictionary(value)
        with open(self.__file_path, 'w') as f:
            json.dump(dictionary_of_dicts, f)
        f.close()

    def from_dictionary(self, dictionary):
        for key, value in dictionary.items():
            class_name = key.split(".", 0)
        obj = eval(class_name)
        obj.__dict__.update(value)
        return obj

    def reload(self):
        """
        deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ;
        otherwise, do nothing. If the file doesn’t exist, no exception should be raised)
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                dictionary_of_dicts = json.load(f)
            f.close()
            for key, value in dictionary_of_dicts.items():
                self.__objects[key] = self.from_dictionary(value)