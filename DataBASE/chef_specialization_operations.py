import psycopg2
import re

def add_chef_specialization_row(connection):
    chef_phone_number = input("Введите номер телефона повара: ")

    # Проверяем соответствие номера телефона шаблону
    while not re.match(r'^(\+375(29|44|25|33))\d{7}$', chef_phone_number):
        print("Некорректный формат номера телефона. Пожалуйста, введите номер в формате +375XXXXXXXXX.")
        chef_phone_number = input("Введите номер телефона повара: ")

    specialization_id = input("Введите ID специализации: ")

    with connection.cursor() as cursor:
        try:
            cursor.execute(
                "INSERT INTO chef_specialization (chef_phone_number, specialization_id) VALUES (%s, %s)",
                (chef_phone_number, specialization_id)
            )
            print("Row inserted successfully!")
        except psycopg2.Error as e:
            print(f"[INFO] Error while inserting row: {e}")


def delete_chef_specialization_row(connection):
    chef_phone_number = input("Введите номер телефона повара для удаления: ")
    specialization_id = input("Введите ID специализации для удаления: ")

    with connection.cursor() as cursor:
        try:
            cursor.execute(
                "DELETE FROM chef_specialization WHERE chef_phone_number = %s AND specialization_id = %s",
                (chef_phone_number, specialization_id)
            )
            print("Row deleted successfully!")
        except psycopg2.Error as e:
            print(f"[INFO] Error while deleting row: {e}")
