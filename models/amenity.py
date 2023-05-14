#!/usr/bin/python3
"""
It defines one class, `Amenity(),
which sub-classes the `BaseModel()` class.`
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """An amenity provided by a place/house.
    """

    name = ""
