
# -*- coding: utf-8 -*-
 
import tweepy, time, sys

class twitter():

    def __init__( self, CK, CS, AK, AS):
#        CONSUMER_KEY = 'lZnpFhlnvQOXbsNwzAPdhztoC'#keep the quotes, replace this with your consumer key
#        CONSUMER_SECRET = '46lp971kdjVZQbXuOaPMlMDjIHbsoUsqPNHUXZos15RR2mvwhh'#keep the quotes, replace this with your consumer secret key
#        ACCESS_KEY = '3131736682-fX969caAesosfDGWMqmJxsrEls2zpSg2QNEOqeo'#keep the quotes, replace this with your access token
#        ACCESS_SECRET = 'lHQzXwppY8L0VfV14jULXLv3tWcKa03RWDmrruvFt9cz5'#keep the quotes, replace this with your access token secret

        self.CONSUMER_KEY    = CK    
        self.CONSUMER_SECRET = CS 
        self.ACCESS_KEY      = AK    
        self.ACCESS_SECRET   = AS    
        
        self.auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        self.auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
        self.api = tweepy.API(auth)

    def tweet( self, message ):
        try:
            self.api.update_status(status = msg)
        except tweepy.error.TweepError:
            print "TweepError!"
