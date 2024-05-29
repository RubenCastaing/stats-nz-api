from API_requests import Employment_Indicators
import pandas as pd
import sqlite3

# This is the main file for requesting the data from stats nz.
# It puts all the data into the stats_nz_data.db database.
# This gets requested by a scheduler in AWS.
# It requests the data from each of the endpoints.

# Fetch the data
Employment_indicators_df = Employment_Indicators.get_employment_indicators()

# Renaming columns to something readable
Employment_indicators_df.rename(columns={
    'Label1': 'Industry',
    'Label2': 'Type',
    'id':'ID'
}, inplace=True)

# Set pandas to display all columns in DataFrame
pd.set_option('display.max_columns', None)

print(Employment_indicators_df)

# Connect to the SQLite database
conn = sqlite3.connect('stats_nz_data.db')
cursor = conn.cursor()

# Iterate over the DataFrame rows
for index, row in Employment_indicators_df.iterrows():
    # Check if the ID already exists
    cursor.execute("SELECT ID FROM EmploymentData WHERE ID = ?", (row['ID'],))
    data_exists = cursor.fetchone()
    
    if not data_exists:
        # If the ID does not exist, insert the new row with renamed columns
        cursor.execute('''
            INSERT INTO EmploymentData (ID, GeoUnit, Geo, Period, Duration, Industry, Type, Value, Unit, Measure, Multiplier, NullReason)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (row['ID'], row['GeoUnit'], row['Geo'], row['Period'], row['Duration'], row['Industry'], row['Type'], row['Value'], row['Unit'], row['Measure'], row['Multiplier'], row['NullReason']))
        conn.commit()  # Commit the insert
    else:
        print(f"Record with ID {row['ID']} already exists.")

# Close the connection
conn.close()
