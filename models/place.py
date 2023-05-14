#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel


class Place(BaseModel):
    """A place/house in the application.

    It represents a place/house uploaded
    by the users of the application.
    """

    name = ""
    user_id = ""
    city_id = ""
    description = ""
    number_bathrooms = 0
    price_by_night = 0
    number_rooms = 0
    longitude = 0.0
    latitude = 0.0
    max_guest = 0
    amenity_ids = []
