#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """An amenity provided by a place/house.

    Attributes:
        name
    """

    name = ""
