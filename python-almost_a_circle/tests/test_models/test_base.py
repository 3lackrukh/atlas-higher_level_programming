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

    def test_base_id_assignment(self):
        """
            Test ensures automatic id assignment
            in multiple instances.
        """
        b1 = Base()
        b2 = Base()
        self.assertEquals(b2.id, b1.id + 1)

    def test_id_assignment(self):
        """
            Test ensures user specified id functionality.
        """
        b1 = Base(12)
        self.assertEqual(b1.id, 12)

