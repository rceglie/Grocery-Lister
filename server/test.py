import psycopg2 as ps
conn = ps.connect(database = 'hackncdb', host = 'localhost', user = 'postgres', password = '1234', port = '1234')
cursor = conn.cursor()

#cursor.execute("INSERT INTO users (name, password, username, address) VALUES ('test', 'test', 'test', 'test')")
cursor.execute("SELECT * FROM users")
print(cursor.fetchall())

conn.commit()