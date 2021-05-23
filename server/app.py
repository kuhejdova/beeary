import os
from datetime import datetime, timedelta

from flask import Flask, jsonify, request, current_app
from flask_cors import CORS

from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import mimetypes

production = os.getenv('NODE_ENV', default="development")
if production == "production":
    from . import database
    from . import config
else:
    import database
    import config

mimetypes.add_type('text/css', '.css')


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__, static_folder='../dist', static_url_path='/')
app.config.from_object(config.BaseConfig)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


def authenticate(email, password):
    if email is None or password is None:
        return None
    user = database.select_user(email)
    if user is None or not check_password_hash(user[0], password):
        return None
    return user


@app.after_request
def add_header(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS, HEAD'

    return response


@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.errorhandler(404)
def page_not_found(e):
    return app.send_static_file('index.html')


@app.route('/register/', methods=['POST'])
def register():
    data = request.get_json()
    u = database.select_user(data['email'])
    if database.select_user(data['email']) is not None:
        return jsonify({
            'status': 'error',
            'message': 'Tento email je už obsazený.',
            'authenticated': False
        }), 401

    hash = generate_password_hash(data['password'])
    database.insert_user(data['email'], hash)
    return jsonify({
        'status': 'success',
        'user': {'email': data['email'], 'password': hash}
    }), 201


@app.route('/login/', methods=['POST'])
def login():
    data = request.get_json()

    user = authenticate(data['email'], data['password'])

    if not user:
        return jsonify({
            'status': 'error',
            'message': 'Špatné přihlašovací údaje',
            'authenticated': False
        }), 401

    token = jwt.encode({
        'sub': data['email'],
        'iat': datetime.utcnow(),
        'exp': datetime.utcnow() + timedelta(hours=2)
    }, current_app.config['SECRET_KEY'])
    return jsonify({
        'status': 'success',
        'token': token.decode('UTF-8')
    })


# sanity check route
@app.route('/ping', methods=['GET']) 
def ping_pong():
    return jsonify('pong!')


@app.route('/sites', methods=['POST'])
def all_sites():
    data = request.get_json()
    result = database.select_sites(data['email'])
    sites = database.sites_to_jsonify(result)

    return jsonify({
        'status': 'success',
        'sites': sites
    })


@app.route('/add_site', methods=['POST'])
def add_site():
    post_data = request.get_json()
    database.insert_sites(post_data['site_name'], post_data['uid'], post_data['location'])
    return jsonify({
        'status': 'success',
        'message': 'ok'
    })


@app.route('/delete_site', methods=['POST'])
def delete_site():
    post_data = request.get_json()
    database.delete_site(post_data['sid'])
    return jsonify({
        'status': 'success',
        'message': 'ok'
    })


@app.route('/hives', methods=['POST'])
def all_hives():
    sid = request.get_json()
    if sid is not None:
        result = database.select_hives(sid['sid'])
        hives = database.hives_to_jsonify(result)
    else:
        hives = []
    return jsonify({
        'status': 'success',
        'hives': hives
    })


@app.route('/activities', methods=['POST'])
def get_month_activities():
    month = request.get_json()
    if month is not None:
        result = database.select_month(month['month'])
        activities = database.months_to_jsonify(result)
    else:
        month = 1
        result = database.select_hives(month)
        activities = database.hives_to_jsonify(result)
    return jsonify({
        'status': 'success',
        'activities': activities
    })


@app.route('/add_hive', methods=['POST'])
def add_hive():
    post_data = request.get_json()
    database.insert_hive(post_data['hive_name'], post_data['sid'])
    return jsonify({
        'status': 'success',
        'message': 'ok'
    })


@app.route('/delete_hive', methods=['POST'])
def delete_hive():
    post_data = request.get_json()
    database.delete_hive(post_data['hid'])
    return jsonify({
        'status': 'success',
        'message': 'ok'
    })


@app.route('/notes', methods=['POST'])
def get_notes():
    hive = request.get_json()
    if hive is not None:
        result = database.select_notes(hive['hid'])
        notes = database.notes_to_jsonify(result)
    else:
        notes = []
    return jsonify({
        'status': 'success',
        'notes': notes
    })


@app.route('/add_note', methods=['POST'])
def add_note():
    post_data = request.get_json()
    database.insert_notes(post_data['note_text'], post_data['hid'], post_data['note_date'])
    print(post_data['note_text'], post_data['hid'], post_data['note_date'])
    return jsonify({
        'status': 'success',
        'message': 'ok'
    })


@app.route('/delete_note', methods=['POST'])
def delete_note():
    data = request.get_json()
    database.delete_note(data['note_id'])
    return jsonify({
        'status': 'success',
        'message': 'ok'
    })


@app.route('/hive_graph', methods=['POST'])
def get_hive_graph():
    data = request.get_json()
    if data is not None:
        graph_data = database.hive_with_graphs(data['hid'], data['dateFrom'], data['dateTo'])
    else:
        graph_data = []
    return jsonify({
        'status': 'success',
        'graphData': graph_data
    })


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(port=port)

