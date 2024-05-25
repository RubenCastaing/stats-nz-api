import sqlite3

# This file creates a new SQLite database with the desired column names.

def create_database_and_table(db_name):
    # Connect to the SQLite database. It will be created if it does not exist.
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Create a table with the new column names
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS EmploymentData (
            ID TEXT PRIMARY KEY,
            GeoUnit TEXT,
            Geo TEXT,
            Period DATE,
            Duration TEXT,
            Industry TEXT,
            Type TEXT,
            Value REAL,
            Unit TEXT,
            Measure TEXT,
            Multiplier INTEGER,
            NullReason TEXT
        )
    ''')
    conn.commit()  # Commit the changes
    conn.close()  # Close the connection

create_database_and_table('stats_nz_data.db')
