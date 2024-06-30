import sqlite3  
  
# Connect to the database  
conn = sqlite3.connect('instance/site.db')  
cur = conn.cursor()  
  
# List all tables  
cur.execute("SELECT name FROM sqlite_master WHERE type='table';")  
tables = cur.fetchall()  
print("Tables in the database:", tables)  
  
# Querying a specific table (replace 'entries' with your table name)  
cur.execute("SELECT * FROM text_entry;")  
rows = cur.fetchall()  
  
print("\nData in 'text_entry' table:")  
for row in rows:  
    print(row)  
  
# Close the cursor and connection  
cur.close()  
conn.close()  
  
  