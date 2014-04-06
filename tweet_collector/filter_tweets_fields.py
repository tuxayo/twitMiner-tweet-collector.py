'''
Created on 5 avr. 2014

@author: victor
'''

def filter_tweets_fields(tweets):
    
    tweets_filtered = []
    
    for tweet in tweets:
        created_at = tweet['created_at']
        at_screen_name = "@"+str(tweet['user']['screen_name'])
        tweet_text_splited = tweet['text'].split(" ")
        tweet_filtered = [created_at, at_screen_name] + tweet_text_splited
        
        tweets_filtered += [tweet_filtered]
    
    return tweets_filtered