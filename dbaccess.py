

import mysql.connector

def connect_db_user_data():
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="12345",
            database="user_data"
        )

def connect_db_user_db():
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="12345",
            database="user_db"
        )

def fetch_data(student_id):
        print("fetch data")
        db = connect_db_user_data()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM users_profile WHERE student_id = %s", (student_id,))
        result = cursor.fetchone()
        db.close()
        return result


