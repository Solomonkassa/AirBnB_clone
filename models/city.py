#!/usr/bin/python3
"""
It defines one class, `City(),
which sub-classes the `BaseModel()` class.`
"""
from models.base_model import BaseModel


class City(BaseModel):
    """ The city class, contains state ID and name
    """
    name = ""
    state_id = ""
