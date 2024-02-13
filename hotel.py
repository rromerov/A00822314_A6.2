import json
import os


class Hotel:
    reservation_counter = 0

    def __init__(self, filename: str = 'hotels.json'):
        self.filename = filename
        if not self.filename.endswith('.json'):
            self.filename += '.json'

    def create_hotel(self, name: str, location: str, rooms: dict):
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='UTF-8') as file:
                hotels_data = json.load(file)
        else:
            hotels_data = []

        hotel_id = len(hotels_data) + 1
        hotel_info = {'hotel_id': hotel_id, 'name': name, 'location': location,
                      'rooms': rooms, 'reservations': []}
        hotels_data.append(hotel_info)

        with open(self.filename, 'w', encoding='UTF-8') as file:
            json.dump(hotels_data, file, indent=4)

        return 'Hotel created'

    def delete_hotel(self, hotel_name: str):
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
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='UTF-8') as file:
                hotels_data = json.load(file)
                for hotel in hotels_data:
                    if hotel['name'] == hotel_name:
                        return hotel
                return 'Hotel not found'

    def modify_hotel_info(self, hotel_name: str, new_name: str = '',
                          new_location: str = ''):
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

    def reserve_room(self, hotel_name: int, client_name: str,
                     reservation_date: str, room_type: str = 'single'):
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='UTF-8') as file:
                hotels_data = json.load(file)

            hotel_found = False
            for hotel in hotels_data:
                if hotel['name'] == hotel_name:
                    if room_type in hotel['rooms']:
                        if hotel['rooms'][room_type] > 0:
                            self.__class__.reservation_counter += 1
                            reservation_id = self.__class__.reservation_counter
                            hotel['rooms'][room_type] -= 1
                            hotel['reservations'].append({
                                'id': reservation_id,
                                'client_name': client_name,
                                'room_type': room_type,
                                'date': reservation_date})
                            hotel_found = True
                            break
                        return f'No {room_type} rooms available'
                    return f'{room_type} room type not found.'

            if hotel_found:
                with open(self.filename, 'w', encoding='UTF-8') as file:
                    json.dump(hotels_data, file, indent=4)
                return f'{room_type} room reserved.'
            return f'{hotel_name} not found.'
        return 'Hotel information not found, please verify'

    def cancel_reservation(self, hotel_name: str, client_name: str):
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='UTF-8') as file:
                hotels_data = json.load(file)

            hotel_found = False
            for hotel in hotels_data:
                if hotel['name'] == hotel_name:
                    for reservation in hotel['reservations']:
                        if reservation['client_name'] == client_name:
                            hotel['rooms'][reservation['room_type']] += 1
                            hotel['reservations'].remove(reservation)
                            hotel_found = True
                            break

            if hotel_found:
                with open(self.filename, 'w', encoding='UTF-8') as file:
                    json.dump(hotels_data, file, indent=4)
                return f'Reservation for {client_name} cancelled'
            return f'Reservation for {client_name} not found'
        return 'Hotel information not found, please verify'
