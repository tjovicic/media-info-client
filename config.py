from os import environ as env

GOOGLE_CLIENT_URL = str(env.get('GOOGLE_CLIENT_URL', 'http://google-client:3000'))
