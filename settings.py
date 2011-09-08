import oauth2 as oauth
import urllib
import urlparse

CONSUMER_KEY = ''
SECRET_KEY = ''

REQUEST_TOKEN_URL = 'http://www.tumblr.com/oauth/request_token'
AUTHORIZE_URL    = 'http://www.tumblr.com/oauth/authorize'
ACCESS_TOKEN_URL  = 'http://www.tumblr.com/oauth/access_token'

PARAMS = {}
PARAMS['x_auth_username'] = ""
PARAMS['x_auth_password'] = ""
PARAMS['x_auth_mode'] = "client_auth"

BLOG = "yourlog.tumblr.com"

CONSUMER = oauth.Consumer(CONSUMER_KEY, SECRET_KEY)
client = oauth.Client(CONSUMER)
client.add_credentials(PARAMS['x_auth_username'], PARAMS['x_auth_password'])
client.authorizations
client.set_signature_method = oauth.SignatureMethod_HMAC_SHA1()

resp, token = client.request(ACCESS_TOKEN_URL, method = "POST", body = urllib.urlencode(PARAMS))
access_token = dict(urlparse.parse_qsl(token))

TOKEN = oauth.Token(access_token['oauth_token'], access_token['oauth_token_secret'])