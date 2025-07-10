import sqlite3
import bcrypt

def login(username, password):
    try:
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()

        cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
        result = cursor.fetchone()

        if result and bcrypt.checkpw(password.encode(), result[0]):
            print("Login successful!")
        else:
            print("Invalid credentials.")

    except Exception as e:
        print("An error occurred:", e)
    finally:
        conn.close()

username_input = input("Enter username: ")
password_input = input("Enter password: ")
login(username_input, password_input)
