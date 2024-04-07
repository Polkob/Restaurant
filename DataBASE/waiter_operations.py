import re
import psycopg2

def add_waiter_row(connection):
    while True:
        passport_number = input("Введите номер паспорта официанта в формате XXXXXXXA00AA: ")

        # Проверяем соответствие номера паспорта шаблону
        if not re.match(r'^\d{7}[A-Z]\d{2}[A-Z]{2}$', passport_number):
            print("Некорректный формат номера паспорта. Пожалуйста, введите номер в формате XXXXXXXAXXAA.")
            continue  # Продолжаем цикл, чтобы запросить ввод заново
        else:
            break  # Выходим из цикла, если номер введен корректно

    name = input("Введите имя официанта: ")
    gender = input("Введите пол официанта (M/F): ")

    # Проверяем, что введенный пол соответствует формату
    if gender not in ('M', 'F'):
        print("Некорректный формат пола. Пожалуйста, введите 'M' для мужского или 'F' для женского.")
        return

    client_phone = input("Введите номер телефона клиента (если есть): ")

    with connection.cursor() as cursor:
        try:
            cursor.execute(
                "INSERT INTO waiter (passport_number, name, gender, client_phone) VALUES (%s, %s, %s, %s)",
                (passport_number, name, gender, client_phone)
            )
            print("Row inserted successfully!")
        except psycopg2.Error as e:
            print(f"[INFO] Error while inserting row: {e}")


def delete_waiter_row(connection):
    passport_number = input("Введите номер паспорта официанта для удаления: ")
    with connection.cursor() as cursor:
        try:
            cursor.execute(
                "DELETE FROM waiter WHERE passport_number = %s",
                (passport_number,)
            )
            print("Row deleted successfully!")
        except psycopg2.Error as e:
            print(f"[INFO] Error while deleting row: {e}")

