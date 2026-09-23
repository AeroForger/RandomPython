import sqlite3
import re
from InquirerPy import inquirer
sql = sqlite3.connect("users.db")
choice = inquirer.select(
    message="Select an option",
    choices=["Search user","Sign up","Delete a user"],
    pointer=">",
).execute()
try:
    cursor = sql.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL
        )         
    """)

    def sign_up():
        name = ""
        email = ""
        email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        while name == "":
            name = input("Name: ")
            if name == "":
                print("Input a valid name")
                continue
        while True:
            email = input("Email: ")
            if re.match(email_pattern, email):
                break
            print("Input a valid email")

        user_data = (name, email)
        cursor.execute("""
            INSERT INTO users (name, email)
            VALUES(?, ?)
        """,
        user_data
        )
        sql.commit()
        print(f"Added name {name} \n and email {email} \n to the database of users")
    def search():
        name = ""
        email = ""
        while name == "" or email == "":
            name = input("Name: ")
            if name == "":
                print("no name inputted search by email")
                email = input("email: ")
                if email != "":
                    search_type("email", email)
                    break
                else:
                    print("You have to input a name or an email to search")
                    continue
            else:
                search_type("name", name)
                break
    def search_type(field, target):
        if field == "email":
            cursor.execute(
                "SELECT id, name, email FROM users WHERE email = ?",
                (target,)
            )

            result = cursor.fetchall()
            print(result)
        else:
            cursor.execute(
                "SELECT id, name, email FROM users WHERE name = ?",
                (target,)
            )

            result = cursor.fetchall()
            print(result)
    def remove():
        name = ""
        email = ""
        email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        while name == "":
            name = input("Name: ")
            if name == "":
                print("Input a valid name")
                continue
        while True:
            email = input("Email: ")
            if re.match(email_pattern, email):
                break
            print("use a valid email")
        query = "SELECT id, name, email FROM users WHERE email = ? AND name = ?"
        user_data = (email, name)
        cursor.execute(query, user_data)
        match = cursor.fetchall()

        if match:
            for row in match:
                delete_command = "DELETE FROM users WHERE id = ?"
                print(f"deleted id {row[0]}")
                cursor.execute(delete_command, (row[0],))
                sql.commit()
        else:
            print("user not found")

    commands = {
        "Search user": search,
        "Sign up": sign_up,
        "Delete a user": remove
    }
    commands[choice]()
except sqlite3.Error as Error:
    print(f"Error: {Error}")
finally:
    if sql:
        sql.close()
        print("Database connection closed.")
        
