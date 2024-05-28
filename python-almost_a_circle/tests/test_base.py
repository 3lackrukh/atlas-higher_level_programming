#!/usr/bin/python3
import os
import json
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


if __name__ == "__main__":
        unittest.main()

class TestBase(unittest.TestCase):
    """
        This module defines test methods for the object class Base.
    """
    def setUp(self):
        """
            This method is called before each test.
            Ensures Base class number of instances is refreshed.
        """
        Base._Base__nb_objects = 0

    def test_base_id_empty(self):
        """
            Test ensures automatic id assignment
        """
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_base_id(self):
        """
            Test ensures user specified id functionality
        """
        b1 = Base(98)
        self.assertEqual(b1.id, 98)    
    
    def test_base_id_type(self):
        """
            Test ensures id is of type int.
        """
        b = Base(1000)
        b1 = Base()
        self.assertIsInstance(b.id, int)
        self.assertIsInstance(b1.id, int)

    def test_nb_objects_increment(self):
         """
         Test ensures __nb_objects increments as expected
         """
         b1 = Base()
         b2 = Base()
         self.assertEqual(Base._Base__nb_objects, 2)

    def test_to_json_string_none(self):
         """
            Test ensures empty input to to_json_string
            returns empty list.
         """
         self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string(self):
        """
            Test ensures to_json_string returns
            a list of dictionaries.
        """
        dict1 = {"id": 1, "width": 10, "height": 20}
        dict2 = {"id": 2, "width": 20, "height": 10}
        dicts = [dict1, dict2]
        self.assertEqual(Base.to_json_string([dict1]), json.dumps([dict1]))
        self.assertEqual(Base.to_json_string(dicts), json.dumps(dicts))

    def test_save_to_file(self):
        """
            Test ensures save_to_file writes JSON string to file.
        """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2,4)
        Rectangle.save_to_file([r1, r2])
        self.assertEqual