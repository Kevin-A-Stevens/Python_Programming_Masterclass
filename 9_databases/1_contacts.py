import sqlite3

# Create a DB connection
db = sqlite3.connect("contacts.sqlite")

# Create a table
db.execute("CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone INTEGER, email TEXT)")

# Insert a records into the table
db.execute("INSERT INTO contacts (name, phone, email) VALUES ('Kevin', '123467890', 'kev@email.com')")
db.execute("INSERT INTO contacts VALUES('Sarah', '1235679087', 'sarah@email.com')")

# Create a cursor used to query the DB
cursor = db.cursor()

# Query the DB
cursor.execute("SELECT * FROM contacts")

# print(cursor.fetchall())
print(cursor.fetchone())  # retrieve a single row

for name, phone, email in cursor:
    print(name)
    print(phone)
    print(email)
    print("-" * 20)

# Close the cursor
cursor.close()

# Commit changes to the DB
db.commit()

# Close DB connection
db.close()
