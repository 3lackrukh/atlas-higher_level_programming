#!/usr/bin/python3
"""
    This module defines test methods for the object class Base.
"""

import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase(unittest.TestCase):
    """
        This module defines test methods for the object class Base.
    """
    def setUp(self):
        """
            This method resets object counter to 0
        """
        Base._Base__nb_objects = 0

    def test_id(self):
        """
            Test ensures automatic id asignment
        """
        b1 = Base()
        self.assertEqual(b1.id, 1)

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
