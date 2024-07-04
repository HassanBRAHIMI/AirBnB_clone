#!/usr/bin/python3
import json
import os
"""a model that will contain the class FileStorage"""


class Filestorage:
    """a class that will take care of serialization and desrialization"""
    __file_path = "../json_files/first.json"
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

    def from_dict_to_jsonstr(self, dict):
        """as it's name says"""
        return json.dumps(dict)
    
    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        list_of = []
            
        with open(self.__file_path, 'w') as f:
            json.dump(self.__objects, f)
        f.close()

    def reload(self):
        """
        deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ;
        otherwise, do nothing. If the file doesn’t exist, no exception should be raised)
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                self.__objects = json.load(f)