import os

from flask import Flask
from flask_cors import CORS
from pymediainfo import MediaInfo
import requests

import config

app = Flask(__name__)
CORS(app)


@app.route('/file/<file_id>')
def main(file_id):
    media_info = get_media_info(file_id)

    return media_info.to_json(), 200


def get_file(file_id):
    response = requests.get(f'{config.GOOGLE_CLIENT_URL}/file/{file_id}')
    return response.json()


def get_media_info(file_id):
    media_info = MediaInfo.parse(f'{config.GOOGLE_CLIENT_URL}/stream/file/{file_id}')

    return media_info


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 3000)), debug=True)
