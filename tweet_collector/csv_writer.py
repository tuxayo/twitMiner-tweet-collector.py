'''
Created on 6 avr. 2014

@author: victor
'''
import logging
import csv

def write_tweets_to_csv_file(tweets, query):
    DIALECT = "unix"
    
    file_name = "query_" + query + "_tweets_"+ str(len(tweets)) + "_dialect_"+str(DIALECT)+".csv"
    
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file, DIALECT)
        writer.writerows(tweets)
    
    logging.info("tweets writen to " + file_name)