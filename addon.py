import xbmc
import xbmcaddon
 
__addon__       = xbmcaddon.Addon()
__addonname__   = __addon__.getAddonInfo('name')
__icon__        = __addon__.getAddonInfo('icon')
 
line1 = "This is a simple example of notifications"
time = 5000  #in miliseconds
 
xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%(__addonname__,line1, time, __icon__))

# import oauth2 as oauth
# import urlparse 
# 
# consumer_key           = "CONSUMER_KEY"
# consumer_secret        = "CONSUMER_SECRET"
# consumer = oauth.Consumer(consumer_key, consumer_secret)
# client = oauth.Client(consumer)
#
#
# request_token_url      = 'https://api.linkedin.com/uas/oauth/requestToken'
# resp, content = client.request(request_token_url, "POST")
# if resp['status'] != '200':
#    raise Exception("Invalid response %s." % resp['status'])
# 
# request_token = dict(urlparse.parse_qsl(content))
#
#
# print "Request Token:"
# print "    - oauth_token        = %s" % request_token['oauth_token']
# print "    - oauth_token_secret = %s" % request_token['oauth_token_secret']
# print 
#
#
# Provider redirect
# authorize_url =      'https://api.linkedin.com/uas/oauth/authorize'
# print "Go to the following link in your browser:"
# print "%s?oauth_token=%s" % (authorize_url, request_token['oauth_token'])
# print 
