""""
This module contains the tests for the Customer class.
"""
import unittest
from categories.hotel import Hotel
from categories.customer import Customer


class TestCreateCustomer(unittest.TestCase):
    """
    Test case for the create customer methods
    """
    def setUp(self):
        self.hotel = Hotel('hotel.json')
        self.hotel.create_hotel(
            'Marriot Space Center',
            'Houston, Texas',
            {'single': 2, 'double': 1,
             'suite': 3}
             )
        self.customer = Customer('hotel.json')

    def test_create_customer(self):
        """
        Test create customer method
        """
        self.assertEqual(
            self.customer.create_customer('Marriot Space Center', 'John Doe'),
            'Customer John Doe created for Marriot Space Center'
            )

    def test_create_customer_hotel_not_found(self):
        """
        Test create customer method with hotel not found
        """
        self.assertEqual(
            self.customer.create_customer('Hilton', 'John Doe'),
            'Customer John Doe not created. Hotel Hilton not found'
            )
