import psycopg2 as ps
conn = ps.connect(database = 'hackncdb', host = 'localhost', user = 'postgres', password = '1234', port = '1234')
cursor = conn.cursor()
from flask import Blueprint, request, make_response, jsonify
import json
from flask_cors import cross_origin
from geopy.distance import geodesic


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
        farStores = []
        for store in storeLocations:
            sid = store[0]
            lat = store[1]
            lon = store[2]
            distance = geodesic(userLocation, (lat, lon)).miles
            if distance > maxDistance: 
                farStores.append(sid)
        cursor.execute('''SELECT * FROM items, stores 
        WHERE sid = stores.id
        AND LOWER(items.name) LIKE %s 
        AND chain NOT IN %s
        AND sid NOT IN %s
        ORDER BY price ASC''', 
        ("%" + data['query'] + "%", tuple(data['exclude']), tuple(farStores)))

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
        cursor.execute("SELECT id FROM users WHERE username = %s AND password = %s", (data["username"],data["password"]))
        result = cursor.fetchone()
        if result == None:
            response.data = "error"
        else:
            response.data = str(result[0])
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
