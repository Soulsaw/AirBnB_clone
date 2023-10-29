#!/usr/bin/python3
"""This class represente some User in our models
"""
from models.base_model import BaseModel


class User(BaseModel):
    """This User class inherit from BaseModel Class
    This class inherit from all methods inside the BaseModel class
    Args:
        email(str): The email of the user
        password(str): The password of the user
        first_name(str): The first_name of the user
        last_name(str): The last_name of the user
    """
    email = ''
    password = ''
    first_name = ''
    last_name = ''
