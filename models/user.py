#!usr/bin/python3
from models.base_model import BaseModel
"""This module defines a class User"""

class User(BaseModel):
    """Creates a new user"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
