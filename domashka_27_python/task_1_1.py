import psycopg2
from random import randint
def connect_db():
    return psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="postgres",
        host="localhost",
        port="5432"
    )

def create_table():
    with connect_db() as conn:
        with conn.cursor() as cur:  
            cur.execute("""
                CREATE TABLE IF NOT EXISTS Salary (
                    id SERIAL PRIMARY KEY,
                    salary_amount NUMERIC
                )
            """)

def insert_data(salary):
    try:
        with connect_db() as conn:
            with conn.cursor() as cur:
                cur.execute("INSERT INTO Salary (salary_amount) VALUES (%s)", (salary,))
    except psycopg2.Error as e:
        print("Ошибка:", e)

def read_all():
    try:
        with connect_db() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM Salary;")
                rows = cur.fetchall()
                for row in rows:
                    print(row)
    except psycopg2.Error as e:
        print("Ошибка:", e)

def read_stoke(id):
    try:
        with connect_db() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM Salary WHERE id =  %s", (id,))
                one = cur.fetchone()
                print(f'содержимое под номером: {id} = ',one)
    except psycopg2.Error as e:
        print('Ошибка: ', e)

def update_data(id, new_salary):
    try:
        with connect_db() as conn:
            with conn.cursor() as cur:
                cur.execute("UPDATE Salary SET salary_amount = %s WHERE id = %s", (new_salary, id))
                print("Успешное обновление")
    except psycopg2.Error as e:
        print("Ошибка:", e)

def delete_table():
        try:
            with connect_db() as conn:
                with conn.cursor() as cur:
                    cur.execute('DROP  TABLE IF EXISTS Salary')
                    print("Таблица удалена.")
        except psycopg2.Error as e:
            print("Ошибка: ",e)
if __name__ == "__main__":
    create_table() 
    print("Успешная вставка")
    for i in range(10):
        insert_data(randint(1000,10000))
    read_all()
    read_stoke(1)
    update_data(3,"56789")
    # для проверки кода раскоментируйте строчку ниже и закоментируйте все до if main...
    # delete_table()