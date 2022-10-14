#!/usr/bin/python3
"""
Module 6-load_from_json_file with load_from_json_file(filename)
Create an object form a JSON file
"""
import json


def load_from_json_file(filename):
    """
    Create a object with json format
    """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
