#loads pythons built in SQLite tools
import sqlite3
    # creates a connection to the database and returns it
def get_connection():
    connection = sqlite3.connect("rides.db")
    return connection
def create_table():
        connection = get_connection()
        cursor = connection.cursor()
        #creates a table called rides with columns for id, trail, miles, and minutes. The id column is the primary key and will automatically increment for each new ride added. The trail column is a text field that cannot be null, the miles column is a real number that cannot be null, and the minutes column is an integer that cannot be null.
        cursor.execute("CREATE TABLE IF NOT EXISTS rides (id INTEGER PRIMARY KEY, trail TEXT NOT NULL, miles REAL NOT NULL, minutes INTEGER NOT NULL)")
        connection.commit()
        connection.close()

create_table()
connection = get_connection()
print(connection.execute("PRAGMA table_info(rides)").fetchall())
connection.close()

def add_ride(trail, miles, minutes):
      
      connection = get_connection()
      cursor = connection.cursor()
      cursor.execute(
            "INSERT INTO rides (trail, miles, minutes) VALUES (?, ?, ?)",
            (trail, miles, minutes)
      )
      connection.commit()
      connection.close()

def get_rides():
      connection = get_connection()
      rides = connection.execute("SELECT * FROM rides").fetchall()
      connection.close()
      return rides

