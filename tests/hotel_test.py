""""
This module contains the tests for the Hotel class.
"""
import unittest
import os
from categories.hotel import Hotel


class TestHotelCreation(unittest.TestCase):
    """
    A class to test the Hotel class.
    """
    def setUp(self):
        """
        Sets up the test environment by creating an instance of the Hotel
        class.
        """
        self.hotel = Hotel('hotels.json')
        self.teardown_called = False

    def tearDown(self):
        """
        Cleans up the test environment by deleting the JSON file if it exists.
        """
        if self.teardown_called and os.path.exists('hotels.json'):
            os.remove('hotels.json')

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
        self.teardown_called = True


class TestHotelDeletion(unittest.TestCase):
    """
    A class to test the deletion of a hotel.
    """
    def setUp(self):
        """
        Sets up the test environment by creating an instance of the Hotel
        class and creating a hotel.
        """
        self.hotel = Hotel('hotel.json')
        self.hotel.create_hotel(
            'St. George Hotel',
            'Tucson Arizona',
            {'single': 2, 'double': 5,
             'suite': 3})
        self.teardown_called = False

    def tearDown(self):
        """
        Cleans up the test environment by deleting the JSON file if it exists.
        """
        if self.teardown_called and os.path.exists('hotel.json'):
            os.remove('hotel.json')

    def test_delete_hotel(self):
        """
        Tests that the delete_hotel method deletes a hotel.
        """
        self.assertEqual(self.hotel.delete_hotel('St. George Hotel'),
                         'Hotel deleted')

    def test_delete_hotel_not_found(self):
        """
        Test delete_hotel method if the hotel doesn't exist.
        """
        self.assertEqual(self.hotel.delete_hotel('St. Adams Hotel'),
                         'Hotel not found')
        self.teardown_called = True


class TestHotelInfo(unittest.TestCase):
    """
    A class to test the info of a hotel.
    """
    def setUp(self):
        """
        Sets up the test environment by creating an instance of the Hotel
        class and creating a hotel.
        """
        self.hotel = Hotel('texas.json')
        self.hotel.create_hotel(
            'Marriot',
            'Houston Texas',
            {'single': 4, 'double': 5,
             'suite': 2})
        self.teardown_called = False

    def tearDown(self):
        """
        Cleans up the test environment by deleting the JSON file if it exists.
        """
        if self.teardown_called and os.path.exists('texas.json'):
            os.remove('texas.json')

    def test_hotel_info(self):
        """
        Tests that the info method returns the hotel information.
        """
        self.assertEqual(self.hotel.display_hotel_info('Marriot'),
                         {'hotel_id': 1, 'name': 'Marriot',
                          'location': 'Houston Texas',
                          'rooms': {'single': 4, 'double': 5, 'suite': 2},
                          'reservations': [], 'customers': []})

    def test_hotel_info_not_found(self):
        """
        Tests the info method if the hotel is not found.
        """
        self.assertEqual(self.hotel.display_hotel_info('St. Adams Hotel'),
                         'Hotel not found')
        self.teardown_called = True
