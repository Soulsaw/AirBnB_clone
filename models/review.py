#!/usr/bin/python3
"""This class represente the review of some User
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """This class inherit from BaseModel class
    Args:
        place_id(str): it will be the Place.id
        user_id(str): it will be the User.id
        text(str): A little description of the review
    """
    place_id = ''  # it will be the Place.id
    user_id = ''  # it will be the User.id
    text = ''
