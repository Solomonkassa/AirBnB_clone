#!/usr/bin/python3
"""
It defines one class, `State(),
which sub-classes the `BaseModel()` class.`
"""
from models.base_model import BaseModel


class State(BaseModel):
    """A state in the application.
    """
    name = ""
