import sqlite3

conn = sqlite3.connect('database.db')
print "Opened database successfully";

conn.execute('CREATE TABLE contact (project TEXT, supplier TEXT, communication INTEGER,recommendation INTEGER,plan INTEGER,expertise INTEGER,quality INTEGER, deadline INTEGER,overall INTEGER,feedback TEXT, email TEXT)')
print "Table created successfully";
conn.close()
