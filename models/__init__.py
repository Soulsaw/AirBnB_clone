#!/usr/bin/python3

"""This module permit to reload the old content of the file to the
to the public class attribute __objects in the FileStorage Module
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
