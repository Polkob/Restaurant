import psycopg2
import re

def add_specialization_row(connection):
    name = input("Введите название специализации: ")

    while True:
        salary = input("Введите зарплату для этой специализации: ")

        # Проверяем, что зарплата является числом с плавающей точкой
        try:
            salary = float(salary)
        except ValueError:
            print("Некорректный формат зарплаты. Пожалуйста, введите число.")
            continue

        # Проверяем, что зарплата больше либо равна нулю
        if salary < 0:
            print("Зарплата должна быть неотрицательным числом.")
            continue
        else:
            break  # Выходим из цикла, если зарплата введена корректно

    with connection.cursor() as cursor:
        try:
            cursor.execute(
                "INSERT INTO specialization (name, salary) VALUES (%s, %s)",
                (name, salary)
            )
            print("Row inserted successfully!")
        except psycopg2.Error as e:
            print(f"[INFO] Error while inserting row: {e}")


def delete_specialization_row(connection):
    specialization_id = input("Введите ID специализации для удаления: ")
    with connection.cursor() as cursor:
        try:
            cursor.execute(
                "DELETE FROM specialization WHERE specialization_id = %s",
                (specialization_id,)
            )
            print("Row deleted successfully!")
        except psycopg2.Error as e:
            print(f"[INFO] Error while deleting row: {e}")
