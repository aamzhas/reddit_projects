#!/usr/bin/env python

"""
Functions that help in extracting data from Game of Thrones Related subreddits.
"""

import csv

import reddit_helpers

__author__ = "Aamir Hasan"
__version__ = "1.0"
__email__ = "hasanaamir215@gmail.com"

bot_name = 'GoT_Crawler'
path = "../data/"
data_filename = "got_crawler_data.csv"


def crawl(reddit, subreddit):
    """
    Crawls through a subreddits comments and writes them into the csv file using the reddit object provided.

    :param reddit: Reddit Instance of the bot
    :param subreddit: The subreddit to be crawled
    """

    data_file = open(path + data_filename, 'a+')
    csv_writer = csv.writer(data_file)

    for comment in reddit.subreddit(subreddit).comments(limit=9999999):
        csv_writer.writerow([comment.id, comment.body, comment.score, comment.subreddit, comment.created])

    data_file.close()


def gather_data():
    """
    Main function that gathers the data for the three popular game of thrones subreddits
    """

    reddit = reddit_helpers.authenticate(bot_name)

    subreddits = ['gameofthrones', 'asoiaf', 'freefolk']

    for subreddit in subreddits:
        crawl(reddit, subreddit)


if __name__ == "__main__":
    gather_data()
