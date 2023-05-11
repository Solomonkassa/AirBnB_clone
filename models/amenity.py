#!/usr/bin/python3
"""The `amenity` module

which sub-classes the `BaseModel()` class.`
It defines one class, `Amenity(),
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """An amenity provided by a place/house.

    Attributes:
        name
    """

    name = ""
