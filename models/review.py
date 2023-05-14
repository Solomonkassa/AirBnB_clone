#!/usr/bin/python3
"""
It defines one class, `Review()`,
which sub-classes the `BaseModel()` class.`
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    It represents a review posted by the users
    of the application about a place/house.
    A review of a place/house.
    """
    text = ""
    user_id = ""
    place_id = ""
