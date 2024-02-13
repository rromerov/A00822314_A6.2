from categories.hotel import Hotel
from categories.customer import Customer
print(Hotel('test1').create_hotel('St. George Hotel', 'Tucson Arizona', {'single': 2, 'double': 5, 'suite': 3}))
print(Hotel('test1').create_hotel('St. Charles Hotel', 'Dallas Texas', {'single': 2, 'double': 5, 'suite': 3}))

customer = Customer('test1.json')
print(customer.create_customer('St. George Hotel', 'John Doe'))
print(customer.create_customer('St. George Hotel', 'Jane Doe'))

print(customer.delete_customer('St. George Hotel', 'Jane Doe'))

print(Hotel('test1').reserve_room('St. George Hotel','Jane Doe', reservation_date='2021-12-25', room_type= 'single'))
print(Hotel('test1').reserve_room('St. George Hotel','John Doe', reservation_date='2021-12-24', room_type= 'suite'))
