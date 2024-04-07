import psycopg2
import re
def add_waiter_table_row(connection):
    while True:
        waiter_passport_number = input("Введите номер паспорта официанта в формате XXXXXXXA00AA: ")

        if not re.match(r'^\d{7}[A-Z]\d{2}[A-Z]{2}$', waiter_passport_number):
            print("Некорректный формат номера паспорта. Пожалуйста, введите номер в формате XXXXXXXAXXAA.")
            continue
        else:
            break
    table_number = input("Введите номер стола: ")

    with connection.cursor() as cursor:
        try:
            cursor.execute(
                "INSERT INTO waiter_table (waiter_passport_number, table_number) VALUES (%s, %s)",
                (waiter_passport_number, table_number)
            )
            print("Row inserted successfully!")
        except psycopg2.Error as e:
            print(f"[INFO] Error while inserting row: {e}")


def delete_waiter_table_row(connection):
    while True:
        waiter_passport_number = input("Введите номер паспорта официанта в формате XXXXXXXA00AA: ")

        if not re.match(r'^\d{7}[A-Z]\d{2}[A-Z]{2}$', waiter_passport_number):
            print("Некорректный формат номера паспорта. Пожалуйста, введите номер в формате XXXXXXXAXXAA.")
            continue
        else:
            break
    table_number = input("Введите номер стола: ")

    with connection.cursor() as cursor:
        try:
            cursor.execute(
                "DELETE FROM waiter_table WHERE waiter_passport_number = %s AND table_number = %s",
                (waiter_passport_number, table_number)
            )
            print("Row deleted successfully!")
        except psycopg2.Error as e:
            print(f"[INFO] Error while deleting row: {e}")
