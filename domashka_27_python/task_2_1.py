"""
Работа с MySQL
# Создание пользователя
CREATE USER 'test_base'@'172.19.0.1' IDENTIFIED BY 'test_base';
# Предоставление привилегий
GRANT ALL PRIVILEGES ON test_base.* TO 'test_base'@'172.19.0.1';
# Применение изменений привилегий
flush_privileges_query = "FLUSH PRIVILEGES;"

"""
import random
import mysql
import mysql.connector
from mysql.connector import Error
from random import randint

def print_rows(rows):
    for row in rows:
        print(row)

def select_from_db(conn, query):
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    return rows

# Подключение к базе данных MySQL
def connect_db():
    return mysql.connector.connect(
        database="test_schema",
        user="root",
        password="postgres",
        host="localhost",  # Предполагается, что PostgreSQL запущен локально
        port="3306",  # Порт по умолчанию для PostgreSQL
    )

# Создание курсора для выполнения SQL-запросов

# cur.execute("GRANT ALL PRIVILEGES ON test_base.* TO 'test_base'@'172.19.0.1';")

# Создание таблицы 'Salary'
def create_table():
    with connect_db() as conn:
        with conn.cursor() as cur: 
            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS Salary (
                    id SERIAL PRIMARY KEY,
                    salary_amount NUMERIC
                )
            """
            )

# Вставка строки без ошибки с использованием транзакции
def insert_data(amount):   
    with connect_db() as conn:
        with conn.cursor() as cur:     
            try:
                # Начало транзакции
                conn.start_transaction()

                # Выполнение вставки
                cur.execute(f"INSERT INTO Salary (salary_amount) VALUES ({amount});")

                # Фиксация транзакции
                conn.commit()

            except Error as e:
                # Откат в случае ошибки
                conn.rollback()
                print("Error:", e)

# Вставка строки с ошибкой и проверка, вставляется ли строка

def read_all():
    with connect_db() as conn:
        with conn.cursor() as cur: 
            try:
                cur.execute("SELECT * FROM Salary;")
                rows = cur.fetchall()
                for row in rows:
                    print(row)
                print()
            except Error as e:
                print("Error READ STROKE:", e)
                if conn.is_connected():
                    cur.close()
                    conn.close()
                    print("Connection closed.")

# Обновление строки и проверка, обновляется ли строка
def update_data(id):
    with connect_db() as conn:
        with conn.cursor() as cur: 
            try:
                cur.execute(
                    f"""
                    UPDATE Salary SET salary_amount = {random.randint(1000, 2000)} WHERE id = {id};
                    """
                )
                print()
                print("update success")

            except Error as e:
                print("Error:", e)
            select_all = "SELECT * FROM Salary;"
            print_rows(select_from_db(conn, select_all))


def read_stroke(id):
    with connect_db() as conn:
        with conn.cursor() as cur: 
            try:
                cur.execute(
                    f"""
                    SELECT * FROM Salary WHERE id = {id};
                """
                )
            except Error as e:
                print("Error READ STROKE:", e)
                if conn.is_connected():
                    cur.close()
                    conn.close()
                    print("Connection closed.")
            print(f'Readed stroke under {id} id is {cur.fetchone()}')
def delete_table():
    with connect_db() as conn:
        with conn.cursor() as cur: 
            cur.execute('DROP TABLE IF EXISTS Salary;')
            print('Table deleted successfully!')
# try:
#     if conn.is_connected():
#         cur.close()
#         conn.close()
#         print("Connection closed.")
# except Error as e:
#     print("Error close:", e)
# finally:
    # cur.close()
    # conn.close()
    # print("Connection closed.")

if __name__ == '__main__':
    create_table()
    for i in range(10):
        insert_data(randint(1000,10000))
    read_all()
    read_stroke(2)
    update_data(5)
    # delete_table()