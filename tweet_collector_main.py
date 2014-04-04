#!/usr/bin/env python3
#from login import login_and_get_twitter

from tweet_collector.login import login_and_get_twitter
from tweet_collector.search_tweets import search_tweets

if __name__ == '__main__':
    twitter = login_and_get_twitter()
    results = search_tweets(query='linux', tweets_per_query=1, twitter=twitter )
    
    #print(results)
    #print (len(results))
    #print(results.keys())
    statuses = results['statuses']
    print(len(statuses))
    next_results_url = results['search_metadata']['next_results']
    print(next_results_url)
