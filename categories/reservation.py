"""
Module for managing hotel reservations.

Uses JSON file for data storage.

Libraries:
- json: Provides functions for reading and writing JSON data.
- Hotel: Class for managing hotel information and reservations.
- Customer: Class for managing customer information within hotels.
"""
import json
from categories.hotel import Hotel
from categories.customer import Customer


class Reservation:
    """
    A class to represent hotel reservations and manage reservation-related
    operations.

    Attributes:
    - hotel_filename (str): The filename for storing hotel data in JSON format.
    - customer (Customer): An instance of the Customer class for managing
    customer information.

    Methods:
    - create_reservation: Creates a new reservation for a customer in a
    specified hotel.
    - cancel_reservation: Cancels a reservation for a customer in a specified
    hotel.
    """
    def __init__(self, hotel_filename: str = 'hotels.json'):
        """
        Initializes a Reservation object with the specified hotel data
        filename.

        Parameters:
        - hotel_filename: The filename for storing hotel data in JSON format.
                          Defaults to 'hotels.json'.
        """
        self.hotel_filename = hotel_filename
        self.customer = Customer(hotel_filename)

    def create_reservation(self, hotel_name: str, customer_name: str,
                           reservation_date: str, room_type: str = 'single'):
        """
        Creates a new reservation for a customer in a specified hotel.

        Parameters:
        - hotel_name: The name of the hotel.
        - customer_name: The name of the customer making the reservation.
        - reservation_date: The date of the reservation.
        - room_type: The type of room to reserve. Defaults to 'single'.

        Returns:
        A string indicating the success of the reservation or a message if the
        room type, hotel, or customer was not found or the reservation could
        not be created.
        """
        hotel = Hotel(self.hotel_filename)

        customer_info = self.customer.display_customer_info(hotel_name,
                                                            customer_name)
        if isinstance(customer_info, dict):
            customer_id = customer_info.get('customer_id')
            if customer_id is None:
                return (
                    f'Customer {customer_name} not found or could not be' 
                    'created'
                )
        else:
            return customer_info

        with open(hotel.filename, 'r', encoding='UTF-8') as file:
            hotels_data = json.load(file)

        for hotel_data in hotels_data:
            if hotel_data['name'] == hotel_name:
                if room_type in hotel_data['rooms']:
                    if hotel_data['rooms'][room_type] > 0:
                        reservation_id = hotel_data.get('reservation_counter', 
                                                        0) + 1
                        hotel_data['reservation_counter'] = reservation_id
                        hotel_data['rooms'][room_type] -= 1
                        reservation = {
                            'id': reservation_id,
                            'customer_id': customer_id,
                            'customer_name': customer_name,
                            'room_type': room_type,
                            'date': reservation_date
                        }
                        hotel_data['reservations'].append(reservation)
                        with open(hotel.filename, 'w',
                                  encoding='UTF-8') as file:
                            json.dump(hotels_data, file, indent=4)
                        return (f'Reservation for {customer_name} created'
                                f' at {hotel_name}')

                    return f'No {room_type} rooms available'

                return f'{room_type} room type not found in {hotel_name}'

        return f'Hotel {hotel_name} not found'

    def cancel_reservation(self, hotel_name: str, customer_name: str):
        """
        Cancels a reservation for a customer in a specified hotel.

        Parameters:
        - hotel_name: The name of the hotel.
        - customer_name: The name of the customer whose reservation is to be
        canceled.

        Returns:
        A string indicating the success of the cancellation or a message if the
        reservation, hotel, or customer was not found.
        """
        hotel = Hotel(self.hotel_filename)

        with open(hotel.filename, 'r', encoding='UTF-8') as file:
            hotels_data = json.load(file)

        for hotel_data in hotels_data:
            if hotel_data['name'] == hotel_name:
                for reservation in hotel_data['reservations']:
                    if reservation['customer_name'] == customer_name:
                        room_type = reservation['room_type']
                        hotel_data['rooms'][room_type] += 1
                        hotel_data['reservations'].remove(reservation)
                        with open(hotel.filename, 'w',
                                  encoding='UTF-8') as file:
                            json.dump(hotels_data, file, indent=4)
                        return (
                            f'Reservation for {customer_name} cancelled at '
                            f'{hotel_name}'
                            )

                return (
                    f'No reservation found for {customer_name} in {hotel_name}'
                )

        return f'Hotel {hotel_name} not found'
