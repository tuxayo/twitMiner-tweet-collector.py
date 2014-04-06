#!/usr/bin/env python3

import twitter
import logging
import sys
from tweet_collector.login import login_and_get_twitter
from tweet_collector.search_tweets import search_tweets
from tweet_collector.filter_tweets_fields import filter_tweets_fields
from tweet_collector.csv_writer import write_tweets_to_csv_file

logging.basicConfig(level=logging.INFO)
    
def display_tweets(tweets):
    for tweet in tweets:
        print(tweet)
        
    print(len(tweets_filtered))

if __name__ == '__main__':
    twitter = login_and_get_twitter()
    query = sys.argv[1]
    tweets = search_tweets(query=query, number_of_queries=int(sys.argv[2]), tweets_per_query=int(sys.argv[3]), twitter=twitter)
    tweets_filtered = filter_tweets_fields(tweets)
#     display_tweets(tweets_filtered)
    
    write_tweets_to_csv_file(tweets_filtered, query=query)
    