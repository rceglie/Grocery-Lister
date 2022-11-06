import psycopg2 as ps
conn = ps.connect(database = 'hackncdb', host = 'localhost', user = 'postgres', password = '1234', port = '1234')
cursor = conn.cursor()

name = "East Franklin Street"
chain = "Trader Joe's"
address = "1800 E Franklin St, Chapel Hill, NC 27514"
#name: string, chain: string, address: string

cursor.execute("INSERT INTO stores (name, chain, address) VALUES (%s, %s, %s)", (name, chain, address))
conn.commit()


cursor.execute('SELECT id FROM stores where name = %s', (name,))
store_id = cursor.fetchone()[0]
print(store_id)
