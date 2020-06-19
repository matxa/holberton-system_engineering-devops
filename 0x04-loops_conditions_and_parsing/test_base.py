import unittest
from models.base import Base
"""Testting Base Class"""


class TestBase(unittest.TestCase):
    """testing 0"""
    def test_id(self):
        b1 = Base()
        r = b1.id
        self.assertEqual(r, 4)
