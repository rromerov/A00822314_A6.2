""""
This module contains the tests for the Hotel class.
"""
import unittest
from categories.hotel import Hotel


class TestHotel(unittest.TestCase):
    """
    A class to test the Hotel class.
    """
    def setUp(self):
        """
        Sets up the test environment by creating an instance of the Hotel
        class.
        """
        self.hotel = Hotel('hotels.json')

    def test_json_creation(self):
        """
        Tests that the JSON file is created when the Hotel class is invoked.
        """
        self.assertEqual(self.hotel.filename, 'hotels.json')

    def test_create_hotel(self):
        """
        Tests that the create_hotel method creates a hotel.
        """
        self.assertEqual(self.hotel.create_hotel(
            'St. George Hotel',
            'Tucson Arizona',
            {'single': 2, 'double': 5,
             'suite': 3}), 'Hotel created')
