#!/usr/bin/python3

"""This class serializes instances to a JSON file and
deserializes JSON file to instances

Authors: @DAVID & @SOULEY
Date: 11/10/2023
"""
import os
import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage():
    """This class serializes instances to a JSON file and deserializes
    JSON file to instances
    This class has two class attributes
    Attributes:
        __file_path (str): file name
        __objects (dict): the dictionary representation of an instance
    """
    __file_path = "file.json"
    __objects = dict()

    def all(self):
        """This method return all the dictionnary objects
        __objects is a class attributes that content the dictionnary
        representation of each class instance
        Returns:
            dict: The dictionnary representation the all instances
        """
        return FileStorage.__objects

    def new(self, obj):
        """This method permit to sets in __objects
        the obj with key <obj class name>.id
        Args:
            obj: Is an object representation of an instance
        Returns:
            nothing just add a new instance object in the __objects attributes
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Thsi method permit to serializes __objects to
        the JSON file (path: __file_path)
        Returns:
            nothing just save the content of the __objects attributes in a file
        """
        my_obj = FileStorage.__objects
        new_dict = {}
        for key, value in my_obj.items():
            new_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, mode='w', encoding='utf-8') as file:
            json.dump(new_dict, file)

    def reload(self):
        """This method permit to deserializes the JSON file
        to __objects (only if the JSON file (__file_path) exists ;
        otherwise, do nothing.If the file doesn’t exist, no exception
        should be raised)
        Return:
            nothing just reload the content of the json file to the
            __objects attributes
        """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, mode='r', encoding='utf-8') \
                        as file:
                json_loads = json.loads(json.dumps(json.load(file)))
                for key, dictionary in json_loads.items():
                    class_name = dictionary['__class__']
                    del dictionary['__class__']
                    json_loads[key] = eval(class_name)(**dictionary)
                FileStorage.__objects = json_loads
