import psycopg2
import re

def add_order_client_row(connection):
    dish_name = input("Введите название блюда: ")

    # Проверяем, что название блюда не пустое
    while not dish_name:
        print("Название блюда не может быть пустым.")
        dish_name = input("Введите название блюда: ")

    # Проверяем, что название блюда не повторяется
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT dish_name FROM order_client WHERE dish_name = %s",
            (dish_name,)
        )
        if cursor.fetchone():
            print("Заказ с таким названием уже существует.")
            return

    client_phone_number = input("Введите номер телефона клиента: ")

    # Проверяем соответствие номера телефона клиента шаблону
    while not re.match(r'^(\+375(29|44|25|33))\d{7}$', client_phone_number):
        print("Некорректный формат номера телефона. Пожалуйста, введите номер в формате +375XXXXXXXXX.")
        client_phone_number = input("Введите номер телефона клиента: ")

    status = input("Выберите статус заказа (pending, processing, completed, cancelled): ")

    # Проверяем, что выбранный статус корректен
    while status not in ('pending', 'processing', 'completed', 'cancelled'):
        print("Некорректный статус заказа.")
        status = input("Выберите статус заказа (pending, processing, completed, cancelled): ")

    with connection.cursor() as cursor:
        try:
            cursor.execute(
                "INSERT INTO order_client (dish_name, client_phone_number, status) VALUES (%s, %s, %s)",
                (dish_name, client_phone_number, status)
            )
            print("Row inserted successfully!")
        except psycopg2.Error as e:
            print(f"[INFO] Error while inserting row: {e}")


def delete_order_client_row(connection):
    order_id = input("Введите номер заказа для удаления: ")

    with connection.cursor() as cursor:
        try:
            cursor.execute(
                "DELETE FROM order_client WHERE order_id = %s",
                (order_id,)
            )
            print("Row deleted successfully!")
        except psycopg2.Error as e:
            print(f"[INFO] Error while deleting row: {e}")
