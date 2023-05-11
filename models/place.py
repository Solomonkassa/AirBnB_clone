#!/usr/bin/python3
"""The `place` module

which sub-classes the `BaseModel()` class.`
It defines one class, `Place(),
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """A place/house in the application.

    Attributes:
        name
        user_id
        city_id
        description
        number_bathrooms
        price_by_night
        number_rooms
        longitude
        latitude
        max_guest
        amenity_ids
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
