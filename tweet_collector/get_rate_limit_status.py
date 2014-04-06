'''
Created on 4 avr. 2014

@author: victor
'''


def get_rate_limit_status(twitter):
    rate_limit_status_application = twitter.application.rate_limit_status()['resources']['search']['/search/tweets']
    return rate_limit_status_application