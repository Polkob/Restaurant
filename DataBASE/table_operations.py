import psycopg2

def add_table_row(connection):
    location = input("Выберите расположение (window, entrance, middle, bar): ")
    capacity = input("Введите вместимость стола: ")

    with connection.cursor() as cursor:
        try:
            cursor.execute(
                "INSERT INTO \"table\" (location, capacity) VALUES (%s, %s)",
                (location, capacity)
            )
            print("Row inserted successfully!")
        except psycopg2.Error as e:
            print(f"[INFO] Error while inserting row: {e}")


