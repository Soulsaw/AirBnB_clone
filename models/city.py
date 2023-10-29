#!/usr/bin/python3
"""This class represented some city in our model
"""
from models.base_model import BaseModel


class City(BaseModel):
    """This class represented some city in our model
    Args:
    :param state_id(str): it will be the State.id
    :param name(str): The name of the city
    """
    state_id = ''  # it will be the State.id
    name = ''
