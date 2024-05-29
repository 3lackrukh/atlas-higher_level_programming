#!/usr/bin/python3
""" Unittest module for Base class """
import unittest
import os
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """This module defines test methods for the object class Base."""
    def setUp(self):
        """This method resets object counter to 0"""
        Base._Base__nb_objects = 0

    def test_id(self):
        """Test ensures automatic id assignment"""
        base = Base()
        self.assertEqual(base.id, 1)
