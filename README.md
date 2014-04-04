twitMiner-tweet-collector.py
============================

Application used to extract data from twitter to a csv file that will be used in a data mining project for university:
[https://github.com/IUTInfoAix/twitMiner/blob/master/Sujet.md](https://github.com/IUTInfoAix/twitMiner/blob/master/Sujet.md)

## Dependencies installation
sudo pip install twitter

OR

sudo easy_install twitter

## Launch for the first time
- Place your credentials and app name in ./twitter\_credentials.txt (see ./twitter\_credentials.txt.example)
- from this directory, run:

python3 tweet\_collector/tweet\_collector_main.py

## Version 0.2.1
What works:

- logs in to Twitter
- get data from a user

### Credits
Inspired by [http://tutorials.iq.harvard.edu/twitter](http://tutorials.iq.harvard.edu/twitter)

### License
GPLv3
