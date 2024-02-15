"""
Module for managing hotel information and reservations.

Uses JSON file for data storage.

Libraries:
- json: Provides functions for reading and writing JSON data.
- os: Provides functions for interacting with the operating system.
"""

import json
import os


class Hotel:
    """
    A class to represent a hotel and manage its information and reservations.

    Attributes:
    - reservation_counter (int): A class attribute to keep track of the
    reservation count.
    - filename (str): The filename for storing hotel data in JSON format.

    Methods:
    - create_hotel: Creates a new hotel entry in the JSON file.
    - get_customer_id: Retrieves the ID of a customer from the hotel's
    customer list.
    - delete_hotel: Deletes a hotel entry from the JSON file.
    - display_hotel_info: Displays information about a specific hotel.
    - modify_hotel_info: Modifies information about a specific hotel.
    - reserve_room: Reserves a room in a specific hotel for a customer.
    - cancel_reservation: Cancels a reservation for a customer in a specific
    hotel.
    """
    reservation_counter = 0

    def __init__(self, filename: str = 'hotels.json'):
        self.filename = filename
        if not self.filename.endswith('.json'):
            self.filename += '.json'

    def create_hotel(self, name: str, location: str, rooms: dict):
        """
        Creates a new hotel entry in the JSON file.

        Parameters:
        - name: The name of the hotel.
        - location: The location of the hotel.
        - rooms: A dictionary containing room types and their quantities.

        Returns:
        A string indicating the success of the operation.
        """
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='UTF-8') as file:
                hotels_data = json.load(file)
        else:
            hotels_data = []

        hotel_id = len(hotels_data) + 1
        hotel_info = {'hotel_id': hotel_id, 'name': name, 'location': location,
                      'rooms': rooms, 'reservations': [], 'customers': []}
        hotels_data.append(hotel_info)

        with open(self.filename, 'w', encoding='UTF-8') as file:
            json.dump(hotels_data, file, indent=4)

        return 'Hotel created'

    def get_customer_id(self, hotel_name: str, customer_name: str):
        """
        Retrieves the ID of a customer from the hotel's customer list.

        Parameters:
        - hotel_name: The name of the hotel.
        - customer_name: The name of the customer.

        Returns:
        The ID of the customer if found, otherwise None.
        """
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='UTF-8') as file:
                hotels_data = json.load(file)
                for hotel in hotels_data:
                    if hotel['name'] == hotel_name:
                        customers = hotel['customers']
                        for customer in customers:
                            if customer['customer_name'] == customer_name:
                                return customer['customer_id']
                        customer_id = len(customers) + 1
                        customers.append({'customer_id': customer_id,
                                          'customer_name': customer_name})
                        with open(self.filename, 'w',
                                  encoding='UTF-8') as file:
                            json.dump(hotels_data, file, indent=4)
                        return customer_id
                return None
        return None

    def delete_hotel(self, hotel_name: str):
        """
        Deletes a hotel entry from the JSON file.

        Parameters:
        - hotel_name: The name of the hotel to delete.

        Returns:
        A string indicating the success of the operation.
        """
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='UTF-8') as file:
                hotels_data = json.load(file)
                for hotel in hotels_data:
                    if hotel['name'] == hotel_name:
                        hotels_data.remove(hotel)
                        with open(self.filename, 'w',
                                  encoding='UTF-8') as file:
                            json.dump(hotels_data, file, indent=4)
                        return 'Hotel deleted'
                return 'Hotel not found'
        return 'Hotel information not found'

    def display_hotel_info(self, hotel_name: str):
        """
        Displays information about a specific hotel.

        Parameters:
        - hotel_name: The name of the hotel to display information for.

        Returns:
        The information of the hotel if found, otherwise a message indicating
        the hotel was not found.
        """
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='UTF-8') as file:
                hotels_data = json.load(file)
                for hotel in hotels_data:
                    if hotel['name'] == hotel_name:
                        return hotel
            return 'Hotel not found'
        return 'Hotel information file not found, please verify'

    def modify_hotel_info(self, hotel_name: str, new_name: str = '',
                          new_location: str = ''):
        """
        Modifies information about a specific hotel.

        Parameters:
        - hotel_name: The name of the hotel to modify.
        - new_name: The new name for the hotel (optional).
        - new_location: The new location for the hotel (optional).

        Returns:
        A string indicating the success of the operation or a message if the
        hotel was not found.
        """
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='UTF-8') as file:
                hotels_data = json.load(file)

            hotel_found = False
            for hotel in hotels_data:
                if hotel['name'] == hotel_name:
                    if new_name:
                        hotel['name'] = new_name
                    if new_location:
                        hotel['location'] = new_location
                    hotel_found = True
                    break

            if hotel_found:
                with open(self.filename, 'w', encoding='UTF-8') as file:
                    json.dump(hotels_data, file, indent=4)
                return 'Hotel information modified'
            return f'{hotel_name} not found'
        return 'Hotel information not found, please verify the file name'

    def reserve_room(self, hotel_name: int, customer_name: str,
                     reservation_date: str, room_type: str = 'single'):
        """
        Reserves a room in a specific hotel for a customer.

        Parameters:
        - hotel_name: The name of the hotel to reserve a room in.
        - customer_name: The name of the customer making the reservation.
        - reservation_date: The date of the reservation.
        - room_type: The type of room to reserve (default is 'single').

        Returns:
        A string indicating the success of the reservation or a message if the
        room type or hotel was not found.
        """
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='UTF-8') as file:
                hotels_data = json.load(file)

            hotel_found = False
            for hotel in hotels_data:
                if hotel['name'] == hotel_name:
                    customer_id = self.get_customer_id(hotel_name,
                                                       customer_name)
                    if customer_id is None:
                        return 'Customer not found or could not be created'
                    if room_type in hotel['rooms']:
                        if hotel['rooms'][room_type] > 0:
                            self.__class__.reservation_counter += 1
                            reservation_id = self.__class__.reservation_counter
                            hotel['rooms'][room_type] -= 1
                            hotel['reservations'].append({
                                'id': reservation_id,
                                'customer_id': customer_id,
                                'customer_name': customer_name,
                                'room_type': room_type,
                                'date': reservation_date})
                            hotel_found = True
                            break
                        return f'No {room_type} rooms available'
                    return f'{room_type} room type not found.'

            if hotel_found:
                with open(self.filename, 'w', encoding='UTF-8') as file:
                    json.dump(hotels_data, file, indent=4)
                return f'{room_type} room reserved for {customer_name}'
            return f'{hotel_name} not found'
        return 'Hotel information not found, please verify'

    def cancel_reservation(self, hotel_name: str, customer_name: str):
        """
        Cancels a reservation for a customer in a specific hotel.

        Parameters:
        - hotel_name: The name of the hotel where the reservation is made.
        - customer_name: The name of the customer whose reservation is to be
        canceled.

        Returns:
        A string indicating the success of the operation or a message if the
        reservation or hotel was not found.
        """
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='UTF-8') as file:
                hotels_data = json.load(file)

            for hotel in hotels_data:
                if hotel['name'] == hotel_name:
                    for reservation in hotel['reservations']:
                        if reservation['customer_name'] == customer_name:
                            room_type = reservation['room_type']
                            hotel['rooms'][room_type] += 1
                            hotel['reservations'].remove(reservation)
                            with open(self.filename, 'w',
                                      encoding='UTF-8') as file:
                                json.dump(hotels_data, file, indent=4)
                            return f'Reservation canceled for {customer_name}'
                    return f'No reservation found for {customer_name}'
            return f'Hotel {hotel_name} not found'
        return 'Hotel information not found, please verify'
