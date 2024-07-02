#!/usr/bin/python3
from datetime import datetime
import uuid
"""this model will contain the super class of everything"""


class BaseModel:
    """the super class of evtg"""
    def __init__(self):
        """the constructor method"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """the __str__ method"""
        return "[{}] [{}] {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """updates the time of last modif"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns the dictionary representation of the obj"""
        nary = self.__dict__.copy()
        nary["__class__"] = self.__class__.__name__
        nary["created_at"] = self.created_at.isoformat()
        nary["updated_at"] = self.updated_at.isoformat()
        return nary
