#!/usr/bin/python3
"""Defining the User module with it's
Attributes
"""
from models.base_model import BaseModel


class User(BaseModel):
    """Represents a user
    Attributes
        email: email of the user
        password: password of the user
        first_name: first name of the user
        last_name: last name of the user
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
