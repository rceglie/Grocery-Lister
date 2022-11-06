import psycopg2 as ps
conn = ps.connect(database = 'hackncdb', host = 'localhost', user = 'postgres', password = '1234', port = '1234')
cursor = conn.cursor()
from flask import Blueprint, request, make_response, jsonify
import json

bp = Blueprint('sql', __name__)

def add_item(name, price, image, url, sid):
    cursor.execute("INSERT INTO items (name, price, image, url, sid) VALUES (%s, %s, %s, %s, %s)", (name, price, image, url, sid))
    conn.commit() 

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
        cursor.execute("SELECT COUNT(1) from list where uid = %s and pid = %s", (data['uid'], data['pid']))
        isMatch = cursor.fetchone()[0]
        if isMatch == 1:
            cursor.execute("UPDATE list SET quantity = quantity - 1 WHERE pid = %s", (data['pid'],))
            response.data = 'Item quantity updated'
        else:
            response.data = 'Item not in list'
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

def _build_cors_preflight_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    return response

def _corsify_actual_response(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response
