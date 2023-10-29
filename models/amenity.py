#!/usr/bin/python3
"""This class represente Amemity in our models
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """This class inherit from BaseModel class
    Args:
        :param name(str): The name of the Amenity
    """
    name = ''
