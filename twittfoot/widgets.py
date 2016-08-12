from django.conf import settings
from dashing.widgets import Widget, NumberWidget, ListWidget
import twitter
import json as js

def oauth_login():
    # XXX: Go to http://twitter.com/apps/new to create an app and get values
    # for these credentials that you'll need to provide in place of these
    # empty string values that are defined as placeholders.
    # See https://dev.twitter.com/docs/auth/oauth for more information 
    # on Twitter's OAuth implementation.
    f = open("twittfoot/credentials.txt")
    cred = js.loads(f.read())
	
    CONSUMER_KEY = cred['consumer_key']
    CONSUMER_SECRET = cred['consumer_secret']
    OAUTH_TOKEN = cred['oauth_token']
    OAUTH_TOKEN_SECRET = cred['oauth_secret']
    
    auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                               CONSUMER_KEY, CONSUMER_SECRET)
    
    twitter_api = twitter.Twitter(auth=auth)
    return twitter_api

# Sample usage
twitter_api = oauth_login()    

def make_twitter_request(twitter_api_func, max_errors=10, *args, **kw): 
    
    # A nested helper function that handles common HTTPErrors. Return an updated
    # value for wait_period if the problem is a 500 level error. Block until the
    # rate limit is reset if it's a rate limiting issue (429 error). Returns None
    # for 401 and 404 errors, which requires special handling by the caller.
    def handle_twitter_http_error(e, wait_period=2, sleep_when_rate_limited=True):
    
        if wait_period > 3600: # Seconds
            print >> sys.stderr, 'Too many retries. Quitting.'
            raise e
    
        # See https://dev.twitter.com/docs/error-codes-responses for common codes
    
        if e.e.code == 401:
            print >> sys.stderr, 'Encountered 401 Error (Not Authorized)'
            return None
        elif e.e.code == 404:
            print >> sys.stderr, 'Encountered 404 Error (Not Found)'
            return None
        elif e.e.code == 429: 
            print >> sys.stderr, 'Encountered 429 Error (Rate Limit Exceeded)'
            if sleep_when_rate_limited:
                print >> sys.stderr, "Retrying in 15 minutes...ZzZ..."
                sys.stderr.flush()
                time.sleep(60*15 + 5)
                print >> sys.stderr, '...ZzZ...Awake now and trying again.'
                return 2
            else:
                raise e # Caller must handle the rate limiting issue
        elif e.e.code in (500, 502, 503, 504):
            print >> sys.stderr, 'Encountered %i Error. Retrying in %i seconds' % \
                (e.e.code, wait_period)
            time.sleep(wait_period)
            wait_period *= 1.5
            return wait_period
        else:
            raise e

    # End of nested helper function
    
    wait_period = 2 
    error_count = 0 

    while True:
        try:
            return twitter_api_func(*args, **kw)
        except twitter.api.TwitterHTTPError, e:
            error_count = 0 
            wait_period = handle_twitter_http_error(e, wait_period)
            if wait_period is None:
                return
        except URLError, e:
            error_count += 1
            print >> sys.stderr, "URLError encountered. Continuing."
            if error_count > max_errors:
                print >> sys.stderr, "Too many consecutive errors...bailing out."
                raise
        except BadStatusLine, e:
            error_count += 1
            print >> sys.stderr, "BadStatusLine encountered. Continuing."
            if error_count > max_errors:
                print >> sys.stderr, "Too many consecutive errors...bailing out."
                raise


class TwitterWidget(ListWidget):
    
    title = 'Twitter Followers'
    #users = 

    users = ['Inter', 'realmadriden', 'FCBarcelona', 'FCBayern', 'acmilan', 'manutd']    
    names = [make_twitter_request(twitter_api.users.lookup, screen_name=user)[0]['name'] for user in users]
    followers = [make_twitter_request(twitter_api.users.lookup, screen_name=user)[0]['followers_count'] for user in users]
    tweets = [make_twitter_request(twitter_api.users.lookup, screen_name=user)[0]['statuses_count'] for user in users]
    updated_at = ''
    data = [ {'user': u, 'followers': f, 'tweets': t} for u,f,t in sorted(zip(names,followers,tweets), key = lambda t: t[1], reverse=True)]

    def get_user(self):
        return self.user

    def get_title(self):
        return self.title

    def get_followers(self):
        return self.followers

    def get_updated_at(self):
        return self.updated_at

    def get_data(self):
        return self.data

    def get_context(self):
        return {
            'title': self.get_title(),
            'user': self.get_user(),
            'followers': self.get_followers(),
            'updatedAt': self.get_updated_at(),
            'data': self.get_data(),
        }
