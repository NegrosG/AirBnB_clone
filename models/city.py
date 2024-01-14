#!/usr/bin/python3
"""
Module for the City Class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Represents the city
    Attributes:
    state_id: state id
    name: name of city    
    """
    state_id = ""
    name = ""
