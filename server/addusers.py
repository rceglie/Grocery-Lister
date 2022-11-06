import psycopg2 as ps
conn = ps.connect(database = 'hackncdb', host = 'localhost', user = 'postgres', password = '1234', port = '1234')
cursor = conn.cursor()

name = "Madelyn Andrews"
password = "bruhmoment"
username = 'MadelynAndrews'
address = "1722 Fordham Blvd #105A, Chapel Hill, NC 27541"

cursor.execute("INSERT INTO users (name, password, username, address) VALUES (%s, %s, %s, %s)", (name, password, username, address))
conn.commit()


cursor.execute('SELECT id FROM users where name = %s', (name,))
user_id = cursor.fetchone()[0]
print(user_id)
