'''
Created on 5 avr. 2014

@author: victor
'''
import logging
import datetime
from tweet_collector.login import login_and_get_twitter
from tweet_collector.get_rate_limit_status import get_rate_limit_status

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    twitter = login_and_get_twitter()
    rate_limit = get_rate_limit_status(twitter)
    reset_timestamp = rate_limit['reset']
    reset_date = str(datetime.datetime.fromtimestamp(reset_timestamp))
    queries_remaining = str(rate_limit['remaining'])
    print("remaining: "+ queries_remaining + ", reset at: " + reset_date)
    