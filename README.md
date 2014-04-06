twitMiner-tweet-collector.py
============================

Application in Python 3 used to extract data from twitter to a csv file that will be used in a data mining project for university:
[https://github.com/IUTInfoAix/twitMiner/blob/master/Sujet.md](https://github.com/IUTInfoAix/twitMiner/blob/master/Sujet.md)

## Dependencies installation
- sudo pip install twitter

OR

- sudo easy_install twitter

## Before using for the first time
Place your credentials and app name in ./twitter\_credentials.txt (see ./twitter\_credentials.txt.example)

## Launch
from this directory, run:

- python3 tweet\_collector\_main.py replaceBySearchQuery 30 50

It will run 30 queries of 50 tweets each

Use \ to protect a hashtag of anything else your shell might interpret

## Version 1.0.0

### Check API limit status
python3 print\_rate\_limit\_status.py

### TODO
- Fix number of tweets collected when logging after each query (wrong value for last query)
- Extract the country

### Credits
Inspired by [http://tutorials.iq.harvard.edu/twitter](http://tutorials.iq.harvard.edu/twitter)

### License
GPLv3
