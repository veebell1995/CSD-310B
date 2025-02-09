import mysql.connector

# Using TCP/IP instead of named pipes
config = {
    "user": "root",
    "password": "Fizzliving4!",
    "host": "localhost",  # Use localhost or 127.0.0.1
    "database": "your_database",
    "raise_on_warnings": True
}

try:
    # Try to connect to the MySQL server
    connection = mysql.connector.connect(**config)
    print("Connection successful!")
except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    if connection.is_connected():
        connection.close()
