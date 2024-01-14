#!/usr/bin/python3
"""
Module of the Review class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Represents the reviews
    Atrributes:
    place_id: the place id
    user_id: the user id
    text: the text of reviews 
    """
    place_id = ""
    user_id = ""
    text = ""
