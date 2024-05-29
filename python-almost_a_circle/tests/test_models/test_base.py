#!/usr/bin/python3
"""unittests for base.py"""

import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Test_Base(unittest.TestCase):
    """test the class Base"""

    def test_id(self):
        """can we make a new Base"""
        Base._Base__nb_objects = 0
        base = Base()
        self.assertEqual(base.id, 1)

    def test_make_a_base(self):
        """do the id's make sense"""
        baseA = Base()
        baseB = Base()
        self.assertEquals(baseA.id, baseB.id - 1)

    def test_assign_id(self):
        """can we assign an id ourselves"""
        self.assertEqual(98, Base(98).id)

    def test_makes_a_base(self):
        """another test of making a new Base with default id"""
        self.assertIsNotNone(Base())

    def test_to_json_string(self):
        """
            Test ensures to_json_string returns
            a list of dictionaries in string format.
        """
        dict1 = {"id": 1, "width": 10, "height": 20}
        dict2 = {"id": 2, "width": 20, "height": 10}
        dicts = [dict1, dict2]
        self.assertEqual(Base.to_json_string([dict1]), json.dumps([dict1]))
        self.assertEqual(Base.to_json_string(dicts), json.dumps(dicts))
        self.assertIsInstance(Base.to_json_string(dicts), str)
