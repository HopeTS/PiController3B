import sqlite3

connection = sqlite3.connect("data.db")


with open("schema.sql") as f:
    connection.executescript(f.read())

cursor = connection.cursor()
cursor.execute(
    "INSERT INTO pin (pin_number, pin_name, base_type, current_type", (1, "power", "Power", "Power"))

connection.commit()
connection.close()
