import os

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
    # print(sites)
    return jsonify({
        'status': 'success',
        'sites': sites
    })


@app.route('/add_site', methods=['POST'])
def add_site():
    post_data = request.get_json()
    database.insert_sites(post_data['site_name'], post_data['uid'], post_data['location'])
    # print(post_data['site_name'], post_data['uid'], post_data['location'])
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
        sid = 1
        result = database.select_hives(sid)
        hives = database.hives_to_jsonify(result)
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
    # print(activities)
    return jsonify({
        'status': 'success',
        'activities': activities
    })


@app.route('/add_hive', methods=['POST'])
def add_hive():
    post_data = request.get_json()
    database.insert_hive(post_data['hive_name'], post_data['sid'])
    # print(post_data['site_name'], post_data['uid'], post_data['location'])
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
        # hid = 1
        # result = database.select_month(hid)
        notes = []
    # print(notes)
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


@app.route('/hive_graph', methods=['POST'])
def get_hive_graph():
    data = request.get_json()
    if data is not None:
        graph_data = database.hive_with_graphs(data['hid'], data['dateFrom'], data['dateTo'])
        # graph_data = database.graph_data_for_hid_to_jsonify(result)
    else:
        graph_data = []
        # sid = 1
        # result = database.select_hives(sid)
        # hives = database.hives_to_jsonify(result)
    # print(graph_data)
    return jsonify({
        'status': 'success',
        'graphData': graph_data
    })


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8000))
    app.run()
