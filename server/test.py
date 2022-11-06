import psycopg2 as ps
import requests
conn = ps.connect(database = 'hackncdb', host = 'localhost', user = 'postgres', password = '1234', port = '1234')
cursor = conn.cursor()

#add_store('test','test','test')
#add_item('test',1.00, 1.00, 'test', 'test', 1)
# x = requests.post('http://127.0.0.1:5000/add_to_list', json = {"uid": 1, "pid": 1})
# print(x.text)
# cursor.execute("SELECT * FROM list")
# print(cursor.fetchall())


#Remove Dupes
cursor.execute('SELECT count(name) from items where sid = 26')
print(cursor.fetchall())
cursor.execute('''DELETE FROM items
WHERE id NOT IN (
    SELECT MAX(id) as max_id
    FROM items
    WHERE sid = 26
    GROUP BY name
) AND sid = 26 ''')

cursor.execute('SELECT count(name) from items where sid=26')
print(cursor.fetchall())
conn.commit()


