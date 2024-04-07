import psycopg2
import re

def add_dish_row(connection):
    dish_name = input("Введите название блюда: ")

    # Проверяем, что название блюда не пустое
    while not dish_name:
        print("Название блюда не может быть пустым.")
        dish_name = input("Введите название блюда: ")

    # Проверяем, что название блюда не повторяется
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT dish_name FROM dish WHERE dish_name = %s",
            (dish_name,)
        )
        if cursor.fetchone():
            print("Блюдо с таким названием уже существует.")
            return

    cost = input("Введите стоимость блюда: ")
    weight = input("Введите вес блюда: ")
    chef_phone_number = input("Введите номер телефона повара: ")

    # Проверяем соответствие номера телефона повара шаблону
    while not re.match(r'^(\+375(29|44|25|33))\d{7}$', chef_phone_number):
        print("Некорректный формат номера телефона. Пожалуйста, введите номер в формате +375XXXXXXXXX.")
        chef_phone_number = input("Введите номер телефона повара: ")

    waiter_passport_number = input("Введите номер паспорта официанта в формате 1234567A12BC: ")

    # Проверяем соответствие номера паспорта официанта шаблону
    while not re.match(r'^\d{7}[A-Z]\d{2}[A-Z]{2}$', waiter_passport_number):
        print("Некорректный формат номера паспорта. Пожалуйста, введите номер в формате 1234567A12BC.")
        waiter_passport_number = input("Введите номер паспорта официанта: ")

    with connection.cursor() as cursor:
        try:
            cursor.execute(
                "INSERT INTO dish (dish_name, cost, weight, chef_phone_number, waiter_passport_number) VALUES (%s, %s, %s, %s, %s)",
                (dish_name, cost, weight, chef_phone_number, waiter_passport_number)
            )
            print("Row inserted successfully!")
        except psycopg2.Error as e:
            print(f"[INFO] Error while inserting row: {e}")


def delete_dish_row(connection):
    dish_name = input("Введите название блюда для удаления: ")

    with connection.cursor() as cursor:
        try:
            cursor.execute(
                "DELETE FROM dish WHERE dish_name = %s",
                (dish_name,)
            )
            print("Row deleted successfully!")
        except psycopg2.Error as e:
            print(f"[INFO] Error while deleting row: {e}")
