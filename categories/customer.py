import json
from categories.hotel import Hotel

class Customer:
    def __init__(self, hotel_filename: str = 'hotels.json'):
        self.hotel_filename = hotel_filename

    def create_customer(self, hotel_name: str, customer_name: str):
        hotel = Hotel(self.hotel_filename)
        with open(hotel.filename, 'r', encoding='UTF-8') as file:
            hotels_data = json.load(file)

        for hotel_data in hotels_data:
            if hotel_data['name'] == hotel_name:
                customers = hotel_data['customers']
                customer_id = len(customers) + 1
                customers.append({'customer_id': customer_id,
                                  'customer_name': customer_name})
                with open(hotel.filename, 'w', encoding='UTF-8') as file:
                    json.dump(hotels_data, file, indent=4)
                return f'Customer {customer_name} created for {hotel_name}'

        return f'Hotel {hotel_name} not found'

    def delete_customer(self, hotel_name: str, customer_name: str):
        hotel = Hotel(self.hotel_filename)
        with open(hotel.filename, 'r', encoding='UTF-8') as file:
            hotels_data = json.load(file)

        for hotel_data in hotels_data:
            if hotel_data['name'] == hotel_name:
                customers = hotel_data['customers']
                for customer in customers:
                    if customer['customer_name'] == customer_name:
                        customers.remove(customer)
                        with open(hotel.filename, 'w',
                                  encoding='UTF-8') as file:
                            json.dump(hotels_data, file, indent=4)
                        return f'Customer {customer_name} deleted'

        return f'Customer {customer_name} not found in {hotel_name}'
