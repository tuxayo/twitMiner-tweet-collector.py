# Python 3

def search_tweets(query, tweets_per_query, twitter):
    result = twitter.search.tweets(q=query, count=tweets_per_query)
    return result
