import psycopg2
import re


def add_chef_row(connection):
    while True:
        phone_number = input("Введите номер телефона повара в формате +375XXXXXXXXX: ")

        # Проверяем соответствие номера телефона шаблону
        if not re.match(r'^(\+375(29|44|25|33))\d{7}$', phone_number):
            print("Некорректный формат номера телефона. Пожалуйста, введите номер в формате +375XXXXXXXXX.")
            continue  # Продолжаем цикл, чтобы запросить ввод заново
        else:
            break  # Выходим из цикла, если номер введен корректно

    name = input("Введите имя повара: ")

    while True:
        experience = input("Введите опыт работы повара (в годах): ")

        # Проверяем, что опыт работы является целым неотрицательным числом
        if not experience.isdigit() or int(experience) < 0:
            print("Некорректный формат опыта работы. Пожалуйста, введите неотрицательное целое число.")
            continue  # Продолжаем цикл, чтобы запросить ввод заново
        else:
            break  # Выходим из цикла, если опыт работы введен корректно

    with connection.cursor() as cursor:
        try:
            cursor.execute(
                "INSERT INTO chef (phone_number, name, experience) VALUES (%s, %s, %s)",
                (phone_number, name, experience)
            )
            print("Row inserted successfully!")
        except psycopg2.Error as e:
            print(f"[INFO] Error while inserting row: {e}")


def delete_chef_row(connection):
    phone_number = input("Введите номер телефона повара для удаления: ")
    with connection.cursor() as cursor:
        try:
            cursor.execute(
                "DELETE FROM chef WHERE phone_number = %s",
                (phone_number,)
            )
            print("Row deleted successfully!")
        except psycopg2.Error as e:
            print(f"[INFO] Error while deleting row: {e}")
