"""
This module contains unit tests for the greater_than function.
"""

import unittest
from test import greater_than

class TestGreaterThan(unittest.TestCase):
    """Unit tests for the greater_than function."""

    def setUp(self):
        self.value_a = 15
        self.value_b = 20

    def test_not_greater(self):
        """Test that a > b returns False."""
        self.assertFalse(greater_than(self.value_a, self.value_b))

    def test_greater(self):
        """Test that b > a returns True."""
        self.assertTrue(greater_than(self.value_b, self.value_a))

if __name__ == '__main__':
    unittest.main()

