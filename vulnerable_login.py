import sqlite3

def login(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)

    result = cursor.fetchone()
    if result:
        print("Login successful!")
    else:
        print("Invalid credentials.")

    conn.close()

username_input = input("Enter username: ")
password_input = input("Enter password: ")
login(username_input, password_input)
