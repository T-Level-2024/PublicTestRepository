import sys
import os
sys.path.insert(0, os.path.abspath(
     os.path.join(os.path.dirname(__file__), '..')))

from calculator import add, subtract, multiply, divide
import unittest


class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
    def test_multiply(self):
        self.assertEqual(multiply(4, 5), 20)
    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(10, 0), "Error: Division by zero")


if __name__ == "__main__":
    unittest.main()
