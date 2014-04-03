#!/usr/bin/python3
#from login import login_and_get_twitter

from login import login_and_get_twitter

if __name__ == '__main__':
    twitter = login_and_get_twitter()
    result = twitter.users.show(screen_name='tuxayo')
    print(result)
