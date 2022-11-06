from flask import Flask
from sql import bp as sql_bp
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # This will enable CORS for all routes
app.config['CORS_HEADERS'] = 'Content-Type'


def create_app():
    from sql import bp as sql_bp
    app.register_blueprint(sql_bp)

create_app()

@app.route('/')
def stuff():
    return "home"