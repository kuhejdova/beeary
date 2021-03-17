from flask import Flask, jsonify
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


if __name__ == '__main__':
    app.run()