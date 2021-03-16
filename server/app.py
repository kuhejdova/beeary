from flask import Flask, jsonify
from flask_cors import CORS


SITES = [
    {
        'id': 1,
        'name': 'Metylovice',
        'user': 'Evik',
        'event': 'Žádná nová událost'
    },
{
        'id': 2,
        'name': 'Ostrava',
        'user': 'Evik',
        'event': 'Pokles teploty'
    },
{
        'id': 3,
        'name': 'Brno',
        'user': 'Evik',
        'event': 'Žádná nová událost'
    },
]


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


@app.route('/home', methods=['GET'])
def all_sites():
    return jsonify({
        'status': 'success',
        'sites': SITES
    })


if __name__ == '__main__':
    app.run()