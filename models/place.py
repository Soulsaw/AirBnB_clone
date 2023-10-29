#!/usr/bin/python3
"""This is the description of Place class"""
from models.base_model import BaseModel


class Place(BaseModel):
    """This class describe the place inside a house
    Args:
        city_id (str): Will be the City.id
        user_id (str): Will be the User.id
        name (str): The name of the place
        description (str): The description of the place
        number_rooms (int): The numbers of room in the place
        number_bathrooms (int): The numbers of bathroom in the place
        max_guest (int): The number of maximal guest in the room
        price_by_night (float): The price to stay one night
        latitude (float): The latitude of the place
        longitude (float): The longitude of the place
        amenity_ids (list): The list of amenity we add the same place
    """
    city_id = ''  # it will be the City.id
    user_id = ''  # it will be the User.id
    name = ''
    description = ''
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []  # it will be the list of Amenity.id later
