#!/usr/bin/python3
"""Defining the init module"""
from models.engine.file_storage import FileStorage


storage = FileStorage()

storage.reload()
