#!/usr/bin/python3

"""
module to house a class called Base
"""

import json
import os


class Base:
    """
    Base class for create methods and attributes
    other sub-class can inherit
    """

    __nb_objects = 0

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        to_json_string - method to convert a list
        of dictionaries to json string representation

        Args:
           list_dictionaries: a list of dictionaries that is to
           be converted to json string representation

        Return:
             a string rep. of an empty list if list_dictionaries
             is not provided or empty
             Or a string representation ofthe provided list
             of dictionaries
        """
        if list_dictionaries is None:
            if len(list_dictionaries) == 0:
                return '[]'
        return json.dumps(list_dictionaries, sort_keys=True)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        save_to_file - method to save dictionaries of all
        class object  as to a file

        Args:
           cls: reference to the class itself
           list_object: list of all dictionary objects
           to be saved into the file

        Return:
           Nothing is to be returned therefore None is returned
        """

        if list_objs is None:
            list_obj = []

        filename = cls.__name__ + ".json"

        with open(filename, 'w') as f:
            json_rep = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
            f.write(json_rep)

    def __init__(self, id=None) -> None:
        """
        __init__ - instance initialization of a base instance

        Args:
           self: reference to the instance being created
           id: optional parameter that cater to the supposed
           id of that instance

        Return:
           None is returned
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def from_json_string(json_string):
        """
        from_json_string - a static method
        that returns the list of the JSON
        string representation json_string:

        Args:
        json_string: is a string
        representing a list of dictionaries

        Returns:
        If json_string is None or empty,
        return an empty list Otherwise,
        return the list represented by
        json_string
        """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        create - method that returns an instance with
        all attributes already set

        Args:
           cls: reference to the class
           **dictionary: dictionary element being unpacked

        Return:
           New instance of the provided dictionary
        """

        newInstance = cls(**dictionary)
        newInstance.update(**newInstance.to_dictionary())
        return newInstance

    @classmethod
    def load_from_file(cls):
        """
        load_from_files - method that reads from a file and
        then, returns a list of instances

        Args:
           cls: reference to the class

        Returns:
           an empty list if file doesnt exist or a
           list of instance
        """

        filename = cls.__name__ + '.json'

        if not os.path.exists(filename):
            return []

        with open(filename, 'r') as f:
            json_rep = f.read()
        obj = cls.from_json_string(json_rep)
        instance = [cls.create(**instance) for instance in obj]
        return instance
