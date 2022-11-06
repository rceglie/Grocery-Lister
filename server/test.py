import psycopg2 as ps
import requests
from geopy.distance import geodesic
conn = ps.connect(database = 'hackncdb', host = 'localhost', user = 'postgres', password = '1234', port = '1234')
cursor = conn.cursor()

#add_store('test','test','test')
#add_item('test',1.00, 1.00, 'test', 'test', 1)
# x = requests.post('http://127.0.0.1:5000/add_to_list', json = {"uid": 1, "pid": 1})
# print(x.text)
# cursor.execute("SELECT * FROM list")
# print(cursor.fetchall())


#Remove Dupes
# cursor.execute('SELECT count(name) from items where sid = 26')
# print(cursor.fetchall())
# cursor.execute('''DELETE FROM items
# WHERE id NOT IN (
#     SELECT MAX(id) as max_id
#     FROM items
#     WHERE sid = 26
#     GROUP BY name
# ) AND sid = 26 ''')

# conn.commit()

x = requests.post('http://127.0.0.1:5000/searchquerylowest', json = {"query": "apple", 'exclude' : ['Walmart', "Trader Joe's"], 'uid': 2, 'maxDistance': 5})
print(x.text)

# uid = 2
# cursor.execute("SELECT address from users where id = %s", [uid])
# userLocation = cursor.fetchone()[0]
# cursor.execute("SELECT id, address from stores")
# storeLocations = cursor.fetchall()
# for store in storeLocations:
#     sid = store[0]
    


    


# import requests

# url = "https://api.geoapify.com/v1/geocode/search?text=38%20Upper%20Montagu%20Street%2C%20London%20W1H%201LJ%2C%20United%20Kingdom&lang=en&limit=1&type=postcode&format=json&apiKey=1922d388abac4d2cbf326b05e1ec5449"
          
# response = requests.get(url)
# print(response.json())
# uid = 2
# maxDistance = 5
# cursor.execute("SELECT lat, lon FROM users where id = %s", (uid,))
# userLocation = cursor.fetchone()
# cursor.execute("SELECT id, lat, lon FROM stores")
# storeLocations = cursor.fetchall()
# farStores = []
# for store in storeLocations:
#      sid = store[0]
#      lat = store[1]
#      lon = store[2]
#      distance = geodesic(userLocation, (lat, lon)).miles
#      if distance > maxDistance: 
#         farStores.append(sid)


