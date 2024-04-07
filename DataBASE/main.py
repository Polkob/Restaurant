import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from config import host, user, password, db_name

from table_operations import add_table_row, delete_table_row
from client_operations import add_client_row, delete_client_row
from order_client_operations import add_order_client_row, delete_order_client_row
from waiter_operations import add_waiter_row, delete_waiter_row
from waiter_table_operations import add_waiter_table_row, delete_waiter_table_row
from chef_operations import add_chef_row, delete_chef_row
from specialization_operations import add_specialization_row, delete_specialization_row
from chef_specialization_operations import add_chef_specialization_row, delete_chef_specialization_row
from dish_operations import add_dish_row, delete_dish_row


# Функция для вывода таблицы
def display_table(connection, table_name):
    with connection.cursor() as cursor:
        cursor.execute(
            sql.SQL("SELECT * FROM {}").format(sql.Identifier(table_name))
        )
        rows = cursor.fetchall()
        for row in rows:
            print(row)


# Функция для добавления строки в таблицу(ссылается на функции для отдельных таблиц)
def add_row(connection, table_name):
    if table_name == "table":
        add_table_row(connection)
    elif table_name == "client":
        add_client_row(connection)
    elif table_name == "waiter":
        add_waiter_row(connection)
    elif table_name == "waiter_table":
        add_waiter_table_row(connection)
    elif table_name == "chef":
        add_chef_row(connection)
    elif table_name == "specialization":
        add_specialization_row(connection)
    elif table_name == "chef_specialization":
        add_chef_specialization_row(connection)
    elif table_name == "dish":
        add_dish_row(connection)
    elif table_name == "order_client":
        add_order_client_row(connection)


# Функция для удаления строки из таблицы(ссылается на функции для отдельных таблиц)
def delete_row(connection, table_name):
    if table_name == "table":
        delete_table_row(connection)
    elif table_name == "client":
        delete_client_row(connection)
    elif table_name == "waiter":
        delete_waiter_row(connection)
    elif table_name == "waiter_table":
        delete_waiter_table_row(connection)
    elif table_name == "chef":
        delete_chef_row(connection)
    elif table_name == "specialization":
        delete_specialization_row(connection)
    elif table_name == "chef_specialization":
        delete_chef_specialization_row(connection)
    elif table_name == "dish":
        delete_dish_row(connection)
    elif table_name == "order_client":
        delete_order_client_row(connection)


# Функция для запросов


def main():
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            dbname=db_name
        )
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

        while True:
            print("1. Таблица table")
            print("2. Таблица client")
            print("3. Таблица waiter")
            print("4. Таблица waiter_table")
            print("5. Таблица chef")
            print("6. Таблица specialization")
            print("7. Таблица chef_specialization")
            print("8. Таблица dish")
            print("9. Таблица order_client")
            print("10. Запросы из 4-5 лыбораторной работы")
            print("0. Выход")

            print('\n')
            table_choice = input("Выберите пункт меню для работы: ")

            if table_choice == "1":
                table_name = "table"
            elif table_choice == "2":
                table_name = "client"
            elif table_choice == "3":
                table_name = "waiter"
            elif table_choice == "4":
                table_name = "waiter_table"
            elif table_choice == "5":
                table_name = "chef"
            elif table_choice == "6":
                table_name = "specialization"
            elif table_choice == "7":
                table_name = "chef_specialization"
            elif table_choice == "8":
                table_name = "dish"
            elif table_choice == "9":
                table_name = "order_client"
            elif table_choice == "10":
                queries(connection)
                continue
            elif table_choice == "0":
                break
            else:
                print("Неверный выбор")
                continue

            print('\n')

            while True:
                print("1. Просмотр таблицы")
                print("2. Добавить строку в таблицу")
                print("3. Удалить строку из таблицы")
                print("4. Вернуться в главное меню")
                print('\n')
                action = input("Выберите действие: ")
                print('\n')
                if action == "1":
                    display_table(connection, table_name)
                    print('\n')
                elif action == "2":
                    add_row(connection, table_name)
                    print('\n')
                elif action == "3":
                    delete_row(connection, table_name)
                    print('\n')
                elif action == "4":
                    print('\n')
                    break
                else:
                    print("Неверный выбор")


    except psycopg2.Error as e:
        print("[INFO] Error while working with PostgreSQL:", e)
    finally:
        if connection:
            connection.close()
            print("[INFO] PostgreSQL connection closed.")

if __name__ == "__main__":
    main()
