#!/usr/bin/python3
"""The `review` module.

which sub-classes the `BaseModel()` class.`
It defines one class, `Review(),
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """A review of a place/house.

    Attributes:
        text (str): The text of the review.
        user_id (str): The user id.
        place_id (str): The place id.
    """
    
    text = ""
    user_id = ""
    place_id = ""
