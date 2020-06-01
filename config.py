import os

ENV = os.environ.get('FLASK_ENV')
DEBUG = True if ENV == 'development' else False
ROOT_URL = os.environ.get('FLASK_ROOT_URL')
SECRET_KEY = 'c6a0ed9340f6ff09a5f7f0e78f3b6779b6195453f0a05f1e'
FB_CLIENT_ID = os.environ.get('FACEBOOK_OAUTH_CLIENT_ID')
FB_CLIENT_SECRET = os.environ.get('FACEBOOK_OAUTH_CLIENT_SECRET')
FB_GRAPH_API = 'https://graph.facebook.com/v3.0/'
FB_MSG_API_URL = 'https://graph.facebook.com/v3.0/me/messages'
FB_VERIFY_TOKEN = os.environ.get('FB_VERIFY_TOKEN')
FB_PAGE_ACCESS_TOKEN = os.environ.get('FB_PAGE_ACCESS_TOKEN')