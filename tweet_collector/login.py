# Python 3
import twitter
import sys
import logging

from twitter.oauth import write_token_file, read_token_file
from twitter.oauth_dance import oauth_dance


def login_and_get_twitter():

    # Go to http://twitter.com/apps/new to create an app and get these items
    # See also http://dev.twitter.com/pages/oauth_single_token

    CREDENTIALS_FILE = './twitter_credentials.txt'
    TOKEN_FILE = './twitter_token.oauth'  # in the current directory
#     try:
    (app_name, consumer_key, consumer_secret) = read_credentials_file(CREDENTIALS_FILE)
#     except IOError:
#         print(TOKEN_FILE + " not found")
    
    try:
        (oauth_token, oauth_token_secret) = read_token_file(TOKEN_FILE)
        logging.info('read token from file success')
    except IOError as e:
        logging.info('read token from file failed, requesting new token')
        (oauth_token, oauth_token_secret) = oauth_dance(app_name, consumer_key,
                consumer_secret)
  
        write_token_file(TOKEN_FILE, oauth_token, oauth_token_secret)

    return twitter.Twitter(domain='api.twitter.com', api_version='1.1',
                        auth=twitter.oauth.OAuth(oauth_token, oauth_token_secret,
                        consumer_key, consumer_secret))

def read_credentials_file(filename):
    """
    Read a credentials file and return the app name, consumer key and consumer secret.
    """
    try:
        f = open(filename)
        return f.readline().strip(), f.readline().strip(), f.readline().strip()
        
    except IOError:
        print(filename + ' not found, please create one using '
                    'twitter_credentials.txt.example')
        sys.exit(1)
    
