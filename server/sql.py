import psycopg2 as ps
conn = ps.connect(database = 'hackncdb', host = 'localhost', user = 'postgres', password = '1234', port = '1234')
cursor = conn.cursor()
from flask import Blueprint, request, make_response, jsonify
import json
from flask_cors import cross_origin
from geopy.distance import geodesic
import requests


bp = Blueprint('sql', __name__)

def add_item(name, price, image, url, sid):
    cursor.execute("INSERT INTO items (name, price, image, url, sid) VALUES (%s, %s, %s, %s, %s)", (name, price, image, url, sid))
    conn.commit() 

@bp.route('/searchquerylowest', methods=['POST', 'OPTIONS'])
def searchquerylowest():
    response = make_response()
    if request.method == 'OPTIONS':
        return _build_cors_preflight_response()
    elif request.method == 'POST':
        data = json.loads(request.data) 

        cursor.execute("SELECT lat, lon FROM users where id = %s", (data['uid'],))
        userLocation = cursor.fetchone()

        maxDistance = data['maxDistance']
        
        cursor.execute("SELECT id, lat, lon FROM stores")
        storeLocations = cursor.fetchall()
        farStores = [0]
        for store in storeLocations:
            sid = store[0]
            lat = store[1]
            lon = store[2]
            distance = geodesic(userLocation, (lat, lon)).miles
            print(distance)
            if distance > int(maxDistance): 
                farStores.append(sid)
        print(farStores)
        cursor.execute('''SELECT * FROM items, stores 
        WHERE sid = stores.id
        AND LOWER(items.name) LIKE %s 
        AND chain NOT IN %s
        AND sid NOT IN %s
        ORDER BY price ASC''', 
        ("%" + data['query'] + "%", tuple(data['exclude']), tuple(farStores)))

        response = jsonify(cursor.fetchall())
        print(response.data)
        return _corsify_actual_response(response)

@bp.route('/get_list', methods=['POST', 'OPTIONS', 'GET'])
def get_list():
    response = make_response()
    if request.method == 'OPTIONS':
        return _build_cors_preflight_response()
    elif request.method == 'POST':
        data = json.loads(request.data)
        cursor.execute('''SELECT * FROM list, items, stores
        WHERE list.uid = %s
        AND list.pid = items.id
        AND items.sid = stores.id''', (data['uid'],))
        response = jsonify(cursor.fetchall())
        return _corsify_actual_response(response)

@bp.route('/add_to_list', methods=['POST', 'OPTIONS', 'GET'])
def add_to_list():
    response = make_response()
    if request.method == 'OPTIONS':
        return _build_cors_preflight_response()
    else:
        data = json.loads(request.data)
        cursor.execute("SELECT COUNT(1) from list where uid = %s and pid = %s", (data['uid'], data['pid']))
        isMatch = cursor.fetchone()[0]
        if isMatch == 1:
            cursor.execute("UPDATE list SET quantity = quantity + 1 WHERE pid = %s", (data['pid'],))
            response.data = 'Item already in list, quantity updated'
        else:
            cursor.execute("INSERT INTO list (uid, pid, quantity) VALUES (%s, %s, %s)", (data['uid'], data['pid'], 1))
            response.data = 'Item added to list'
        conn.commit()
        return response
    
@bp.route('/remove_from_list', methods=['POST', 'OPTIONS', 'GET'])
def remove_from_list():
    response = make_response()
    if request.method == 'OPTIONS':
        return _build_cors_preflight_response()
    else:
        data = json.loads(request.data)
        cursor.execute("DELETE FROM list WHERE uid = %s and pid = %s", (data['uid'], data['pid']))
        response.data = 'Item removed from list'
    conn.commit()
    return response

@bp.route('/get_user', methods=['POST', 'OPTIONS', 'GET'])
def get_user():
    response = make_response()
    if request.method == "OPTIONS": # CORS preflight
        return _build_cors_preflight_response()
    else:
        data = json.loads(request.data)
        cursor.execute("SELECT * FROM users WHERE id = %s", (data["uid"],))
        response.data = cursor.fetchone()[0]
        print(response.data)
        return response


@bp.route('/change_password', methods=['POST', 'OPTIONS', 'GET'])
def change_password():
    response = make_response()
    if request.method == "OPTIONS": # CORS preflight
        return _build_cors_preflight_response()
    else:
        data = json.loads(request.data)
        cursor.execute("SELECT password FROM users WHERE id = %s", (data["uid"],))
        if data["oldpass"] == cursor.fetchone()[0]:
            cursor.execute("UPDATE users SET password = %s WHERE id = %s", (data["newpass"], data["uid"]))
            conn.commit()
            response.data = "true"
        else:
            response.data = "true"
        return response

@bp.route('/sign_in', methods=['POST', 'OPTIONS', 'GET'])
def sign_in():
    response = make_response()
    if request.method == "OPTIONS": # CORS preflight
        return _build_cors_preflight_response()
    else:
        data = json.loads(request.data)
        cursor.execute("SELECT id FROM users WHERE username = %s AND password = %s", (data["username"],data["password"]))
        result = cursor.fetchone()
        if result == None:
            response.data = "error"
        else:
            response.data = str(result[0])
        return response

@bp.route('/sign_up', methods=['POST', 'OPTIONS', 'GET'])
def sign_up():
    response = make_response()
    if request.method == "OPTIONS": # CORS preflight
        return _build_cors_preflight_response()
    else:
        data = json.loads(request.data)
        cursor.execute("INSERT into users (name, username, password, address) values (%s, %s, %s, %s)", (data["name"],data["username"],data["password"],""))
        conn.commit()
        cursor.execute("Select id from users where username=%s AND password=%s", (data["username"], data["password"]))
        result = cursor.fetchone()
        if result == None:
            response.data = "error"
        else:
            response.data = str(result[0])
        return response

@bp.route('/change_address', methods=['POST', 'OPTIONS', 'GET'])
def change_address():
    response = make_response()
    if request.method == "OPTIONS": # CORS preflight
        return _build_cors_preflight_response()
    else:
        data = json.loads(request.data)
        address = data['street'] + ", " + data['city'] + ", " + data['state']
        street = data['street'].replace(" ", "%20")
        city = data['city'].replace(" ", "%20")
        state = data['state'].replace(" ", "%20")
        url = "https://api.geoapify.com/v1/geocode/search?text=" \
            + street + "%2C%20" \
            + city + "%2C%20" \
            + state + "%2C%20United%20States%20of%20America&lang=en&limit=1&type=amenity&format=json&apiKey=1922d388abac4d2cbf326b05e1ec5449"
        mapResponse = requests.get(url)
        lon = mapResponse.json()["results"][0]["lon"]
        lat = mapResponse.json()["results"][0]["lat"]
        cursor.execute("UPDATE users SET address = %s, lat = %s, lon = %s WHERE id = %s", (address, lat, lon, data["uid"]))
        conn.commit()
        response.data = "true"
        return response



def _build_cors_preflight_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    return response

def _corsify_actual_response(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response
