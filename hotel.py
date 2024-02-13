import json
import os

class Hotel:

    reservation_counter = 0

    def __init__(self, filename: str):
        self.filename = filename
        if not self.filename.endswith('.json'):
            self.filename += '.json'
        if self.filename.endswith('.json'):
            pass
        if self.filename == '':
            self.filename = 'hotel.json'

    def create_hotel(self, name: str, location: str, rooms: dict):
        with open(self.filename, 'w', encoding='UTF-8') as file:
            try:
                data = ({'name': name,
                         'location': location,
                         'rooms': rooms,
                         'reservations': []})
                json.dump(data, file, indent=4)
                return 'Hotel created'
            except SyntaxError:
                return 'Incorrect data format, please verify'
            
    def delete_hotel(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)
            return 'Hotel deleted'
        return 'Hotel not found, nothing to delete'
    
    def display_hotel_info(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='UTF-8') as file:
                data = json.load(file)
                return data
        return 'Hotel information not found, please verify the file name or create a new hotel.'
    
    def modify_hotel_info(self, name: str = '', location: str = ''):
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='UTF-8') as file:
                data = json.load(file)
                if name != '':
                    data['name'] = name
                if location != '':
                    data['location'] = location
                return 'Hotel information modified', data
        return 'Hotel information not found, please verify the file name or create a new hotel.'
   
    def reserve_room(self, full_name: str, reservation_date: str, room_type: str = 'single'):
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='UTF-8') as file:
                data = json.load(file)
                if room_type in data['rooms']:
                    if data['rooms'][room_type] > 0:
                        self.__class__.reservation_counter += 1
                        reservation_id = self.__class__.reservation_counter
                        data['rooms'][room_type] -= 1
                        data['reservations'].append({'id': reservation_id, 'full_name': full_name, 'room_type': room_type, 'date': reservation_date})
                        with open(self.filename, 'w', encoding='UTF-8') as file:
                            json.dump(data, file, indent=4)
                        return f'{room_type} room reserved'
                    return f'No {room_type} rooms available choose other option please'
                return f'{room_type} room type not found'
        return 'Hotel information not found, please verify the file name or create a new hotel'
 
    def cancel_reservation(self, reservation_id: int):
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='UTF-8') as file:
                data = json.load(file)
                for reservation in data['reservations']:
                    if reservation['id'] == reservation_id:
                        data['rooms'][reservation['room_type']] += 1
                        data['reservations'].remove(reservation)
                        with open(self.filename, 'w', encoding='UTF-8') as file:
                            json.dump(data, file, indent=4)
                        return f'Reservation {reservation_id} cancelled'
                return f'Reservation {reservation_id} not found'
        return 'Hotel information not found, please verify the file name or create a new hotel'
