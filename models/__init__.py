#!/usr/bin/python3
"""Defining the init module"""
from models.engine.file_storage import Filestorage


storage = Filestorage()

storage.reload()
