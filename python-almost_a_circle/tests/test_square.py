#!/usr/bin/python3
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """
        This module defines test methods for the object class Square.
    """

    def test_Square_id(self):
        """
            Test ensures user specified id functionality
            and auto id functionality 
        """
        s1 = Square(2, 0, 0, 12)
        self.assertEqual(s1.id, 12)
        s2 = Square(2, 0, 0, None)
        s3 = Square(1, 0, 0, None)
        self.assertEqual(s2.id, 3)
        self.assertEqual(s3.id, 4)
    
    def test_Square_id_type(self):
        """
            Test ensures id is of type int.
        """
        s = Square(2, 0, 0, 1000)
        s1 = Square(1, 0, 0)
        self.assertIsInstance(s.id, int)
        self.assertIsInstance(s1.id, int)

    def test_Square_size(self):
        s = Square(2, 0, 0)
        self.assertEqual(s.size, 2)
        s1 = Square("2", 0, 0)
        self.assertRaises(TypeError)

    def test_Square_x(self):
        s = Square(1, 12)
        self.assertEqual(s.x, 12)
        s1 = Rectangle(2, "12")
        self.assertRaises(TypeError)
        s2 = Square(1)
        self.assertEqual(s2.x, 0)

    def test_Square_y(self):
        s = Square(1, 0, 4)
        self.assertEqual(s.y, 4)
        s1 = Square(1, 0, "4")
        self.assertRaises(TypeError)
        s2 = Square(3)
        self.assertEqual(s2.y, 0)
