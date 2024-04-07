import re
import psycopg2

def add_client_row(connection):
    while True:
        phone_number = input("Введите номер телефона клиента в формате +375XXXXXXXXX: ")

        # Проверяем соответствие номера телефона шаблону
        if not re.match(r'^(\+375(29|44|25|33))\d{7}$', phone_number):
            print("Некорректный формат номера телефона. Пожалуйста, введите номер в формате +375XXXXXXXXX.")
            continue  # Продолжаем цикл, чтобы запросить ввод заново
        else:
            break  # Выходим из цикла, если номер введен корректно

    name = input("Введите имя клиента: ")
    profession = input("Введите профессию клиента: ")
    table_number = input("Введите номер стола: ")

    with connection.cursor() as cursor:
        try:
            cursor.execute(
                "INSERT INTO client (phone_number, name, profession, table_number) VALUES (%s, %s, %s, %s)",
                (phone_number, name, profession, table_number)
            )
            print("Row inserted successfully!")
        except psycopg2.Error as e:
            print(f"[INFO] Error while inserting row: {e}")


def delete_client_row(connection):
    phone_number = input("Введите номер телефона клиента для удаления: ")
    with connection.cursor() as cursor:
        try:
            cursor.execute(
                "DELETE FROM client WHERE phone_number = %s",
                (phone_number,)
            )
            print("Row deleted successfully!")
        except psycopg2.Error as e:
            print(f"[INFO] Error while deleting row: {e}")
