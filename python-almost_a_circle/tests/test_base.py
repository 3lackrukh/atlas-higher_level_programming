#!/usr/bin/python3

import unittest
import os
import json
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
        self.base = Base()

    def tearDown(self):
        del self.base

    def test_id(self):
        """
            Test ensures automatic id assignment
        """
        self.assertEqual(self.base.id, 1)
