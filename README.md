# Actividad 6.2. Ejercicio de programación 3 y pruebas de unidad

## 1. Reservation System

Para correr exitosamente el programa, es necesario contar con la librería **virtualenv** instalada, en caso de no tenerla, se puede instalar con el siguiente comando:

```
pip install virtualenv
```

Una vez instalada la librería, se debe crear un entorno virtual desde la ruta principal del proyecto, con el siguiente comando:

```
virtualenv venv
```

Posteriormente, se debe activar el entorno virtual con el siguiente comando en **Linux**:

```
source venv/bin/activate
```
Para **Windows**, el comando es el siguiente:

```
venv\Scripts\activate
```

Una vez activado el entorno virtual, se deben instalar las dependencias del proyecto con el siguiente comando (en Linux):

```
pip install -r linux_requirements.txt
```

Para **Windows**, el comando es el siguiente:

```
pip install -r win_requirements.txt
```
Para verificar que **Pylint** no presenta errores, se debe ejecutar el siguiente comando:

```
pylint .
```
Con **Flake8** se escribe en consola:

```
flake8
```
Para ejecutar las pruebas unitarias, se debe ejecutar el siguiente comando en **Linux**:

```
python3 -m unittest discover -s tests -p '*_test.py' -v
```

En **Windows**:
```
python -m unittest discover -s tests -p '*_test.py' -v
```

El resultado debe ser el siguiente:
```
test_create_customer (customer_test.TestCustomer) ... ok
test_create_customer_hotel_not_found (customer_test.TestCustomer) ... ok
test_delete_customer (customer_test.TestCustomer) ... ok
test_delete_customer_not_found (customer_test.TestCustomer) ... ok
test_display_customer_info (customer_test.TestCustomer) ... ok
test_display_customer_info_not_found (customer_test.TestCustomer) ... ok
test_modify_customer_info (customer_test.TestCustomer) ... ok
test_modify_customer_info_not_found (customer_test.TestCustomer) ... ok
test_cancel_reservation_hotel_not_found (hotel_test.TestHotelCancelReservation) ... ok
test_cancel_reservation_not_found (hotel_test.TestHotelCancelReservation) ... ok
test_cancel_reservation_success (hotel_test.TestHotelCancelReservation) ... ok
test_create_hotel (hotel_test.TestHotelCreation) ... ok
test_json_creation (hotel_test.TestHotelCreation) ... ok
test_delete_hotel (hotel_test.TestHotelDeletion) ... ok
test_delete_hotel_not_found (hotel_test.TestHotelDeletion) ... ok
test_hotel_info (hotel_test.TestHotelInfo) ... ok
test_hotel_info_not_found (hotel_test.TestHotelInfo) ... ok
test_modify_hotel (hotel_test.TestHotelModification) ... ok
test_modify_hotel_not_found (hotel_test.TestHotelModification) ... ok
test_reserve_room (hotel_test.TestHotelReservation) ... ok
test_reserve_room_hotel_not_exist (hotel_test.TestHotelReservation) ... ok
test_reserve_room_no_single_available (hotel_test.TestHotelReservation) ... ok
test_cancel_reservation_hotel_not_found (reservation_test.TestReservation) ... ok
test_cancel_reservation_not_found (reservation_test.TestReservation) ... ok
test_cancel_reservation_success (reservation_test.TestReservation) ... ok
test_create_reservation (reservation_test.TestReservation) ... ok
test_create_reservation_hotel_not_found (reservation_test.TestReservation) ... ok
test_create_reservation_no_room_available (reservation_test.TestReservation) ... ok

----------------------------------------------------------------------
Ran 28 tests in 0.185s

OK
```

Para obtener el reporte de cobertura, se debe ejecutar lo siguiente:

```
coverage run -m unittest discover -s tests -p '*_test.py' -v
```
Seguido de:
```
coverage report
```

El resultado debe ser el siguiente:
```

Name                             Stmts   Miss  Cover
----------------------------------------------------
categories\__init__.py               2      0   100%
categories\customer.py              57      0   100%
categories\hotel.py                119     12    90%
categories\reservation.py           41      3    93%
tests\customer_test.py              36      0   100%
tests\hotel_test.py                 94      0   100%
tests\reservation_test.py           36      0   100%
utilities\json_data_handler.py      10      0   100%
----------------------------------------------------
TOTAL                              395     15    96%
```