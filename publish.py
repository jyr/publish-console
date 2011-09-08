from pyblr import pyblr
import oauth2 as oauth
import urllib
import urlparse
from settings import *


client = pyblr.Pyblr(oauth.Client(CONSUMER, TOKEN))

params = {}
params['type'] = "text"
params['body'] = "from publish"

post = client.create_post(BLOG, params)