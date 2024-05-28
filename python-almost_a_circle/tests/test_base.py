#!/usr/bin/python3
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """
        This module defines test methods for the object class Base.
    """

    def test_base_id(self):
        """
            Test ensures user specified id functionality
        """
        b1 = Base(12)
        self.assertEqual(b1.id, 12)

    def test_base_id_empty(self):
        """
            Test ensures automatic id assignment
        """
        b2 = Base()
        b3 = Base()
        self.assertEqual(b2.id, 1)
        self.assertEqual(b3.id, 2)
    
    def test_base_id_type(self):
        """
            Test ensures id is of type int.
        """
        b = Base(1000)
        b1 = Base()
        self.assertIsInstance(b.id, int)
        self.assertIsInstance(b1.id, int)

    if __name__ == "__main__":
        unittest.main()