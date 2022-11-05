import psycopg2 as ps
conn = ps.connect(database = 'hackncdb', host = 'localhost', user = 'postgres', password = '1234', port = '1234')
cursor = conn.cursor()
from flask import Blueprint, request, make_response, jsonify
import json

bp = Blueprint('sql', __name__)

def add_store(name, chain, address):
    cursor.execute("INSERT INTO stores (name, chain, address) VALUES (%s, %s, %s)", (name, chain, address))
    conn.commit()

def add_item(name, price, value, image, url, sid):
    cursor.execute("INSERT INTO items (name, price, value, image, url, sid) VALUES (%s, %s, %s, %s, %s, %s)", (name, price, value, image, url, sid))
    conn.commit()

#def 


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
