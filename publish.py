from pyblr import pyblr
import oauth2 as oauth
import urllib
import urlparse
import sys
from settings import *


def main(*args, **kwargs):
  client = pyblr.Pyblr(oauth.Client(CONSUMER, TOKEN))
  action = sys.argv[1]

  switch = {'post': post,'followers': followers}
  switch[action](client, args)
  
def post(client, args):
  params = {}
  params['type'] = raw_input("Type: ")
  params['body'] = raw_input("Body: ")

  post = client.create_post(BLOG, params)
  print "Done! id: ", post['id']

def followers(client, args):
  followers = client.followers(BLOG)
  print "total users ", followers['total_users']
  
if __name__ == "__main__":
  if len(sys.argv) < 2:
      print "Usage: \n\t python publish.py post|followers"
      sys.exit(1)
  elif len(sys.argv) == 2:
    if sys.argv[1] == 'post' or sys.argv[1] == "followers":
      main(sys.argv)
    else:
      print "Usage: \n\t python publish.py post|followers"
      sys.exit(1)