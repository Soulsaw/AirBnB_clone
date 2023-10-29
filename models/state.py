#!/usr/bin/python3
"""This class describe some state
"""
from models.base_model import BaseModel


class State(BaseModel):
    """This class describe some state but it have one argument
    :param name(str): Is a public instance of class
    """
    name = ''
