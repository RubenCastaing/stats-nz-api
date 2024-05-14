import sqlite3
import pandas as pd

#Example query to a local database. Just for testing

# Connect to the SQLite database
conn = sqlite3.connect('stats_nz_data.db')

# Create a SQL query string
query = "SELECT * FROM EmploymentData WHERE Label1 = 'All industries'"

# Execute the query and store the result in a DataFrame
df = pd.read_sql_query(query, conn)

# Display the DataFrame
print(df)

# Close the connection
conn.close()
