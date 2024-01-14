#!/usr/bin/python3
"""
Module for the Place class
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Represents the Place
    Attributes:
    city_id: the city id
    user_id: the user id
    name: name pof place
    description: description of the place
    number_rooms: number of rooms in place
    number_bathrooms: number of bathrooms
    max_guest: the maximum guest of the place
    price_by_night: price by night of the place
    latitude: latitude of the place
    longitude: longitude of the place
    amenity_id: amenity id
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0
    longitude = 0
    amenity_ids = []
