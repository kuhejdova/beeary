from flask import Flask, jsonify, request
from flask_cors import CORS

import database

# SITES = [
#     {
#         'id': 1,
#         'name': 'Nej uly',
#         'user': 'Evik',
#         'location': 'Metylovice',
#         'event': 'Žádná nová událost'
#     },
# {
#         'id': 2,
#         'name': 'Stanoviste',
#         'user': 'Evik',
#         'location': 'Ostrava',
#         'event': 'Pokles teploty'
#     },
# {
#         'id': 3,
#         'name': 'Study',
#         'user': 'Evik',
#         'location': 'Brno',
#         'event': 'Žádná nová událost'
#     },
# ]


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


@app.after_request
def add_header(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS, HEAD'

    return response

# sanity check route
@app.route('/ping', methods=['GET']) # prepsat na post
def ping_pong():
    return jsonify('pong!')


@app.route('/sites', methods=['GET'])
def all_sites():
    uid = "gXifKfOg06XvU9NewGfqiFwasE12"
    result = database.select_sites(uid)
    sites = database.sites_to_jsonify(result)
    return jsonify({
        'status': 'success',
        'sites': sites
    })


@app.route('/hives', methods=['GET', 'POST'])
def all_hives():
    if request.method == 'POST':
        post_data = request.get_json()
        sid = database.select_site_id(post_data['sid'])[0]
        result = database.select_hives(sid)
        hives = database.hives_to_jsonify(result)
        print(post_data)
        print(hives)
    if request.method == 'GET':
        sid = 1
        result = database.select_hives(sid)
        hives = database.hives_to_jsonify(result)
    return jsonify({
        'status': 'success',
        'hives': hives
    })


if __name__ == '__main__':
    app.run()