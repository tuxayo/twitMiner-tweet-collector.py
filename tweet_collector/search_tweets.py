# Python 3
import logging
from urllib.error import URLError

def search_tweets(query, tweets_per_query, twitter, number_of_queries):
    max_id_for_next_query = None

    tweets = []
    for i in range(0, number_of_queries):
        result = get_tweet_from_api(query=query, count=tweets_per_query, max_id=max_id_for_next_query, twitter=twitter)
        if 'next_results' in result['search_metadata']:
            next_results_url = result['search_metadata']['next_results']
            max_id_for_next_query = get_max_id_from_next_results_url(next_results_url)
        else:
            next_results_url = None
            
        tweets = tweets + result['statuses']
        number_of_queries_done = i + 1
        number_of_tweets_collected = number_of_queries_done * tweets_per_query
        logging.info("Query " + str(number_of_queries_done) + " done, tweets: " + str(number_of_tweets_collected))
        
        if next_results_url is None: # if end of total results
            break

    return tweets
    


def get_max_id_from_next_results_url(url):
    """ Extract max id from an url which looks like this one:
    ?max_id=452159220570669055&q=linux&count=1&include_entities=1"""
    
    max_id_block = url.split("&")[0]
    # now we have something like this: "?max_id=452159701250494463"
    
    max_id = max_id_block.split("=")[1]
    return max_id

def get_tweet_from_api(query, count, max_id, twitter):
    try:
        return twitter.search.tweets(q=query, count=count, max_id=max_id)

    except URLError:
        print("urllib.error.URLError: network problem: Your network sucks!, retring query")
        return get_tweet_from_api(query=query, count=count, max_id=max_id, twitter=twitter)