#!/usr/bin/env python

"""
Functions that help in extracting data from Game of Thrones Related subreddits.
"""

import csv

import reddit_helpers

__author__ = "Aamir Hasan"
__version__ = "1.0.2"
__email__ = "hasanaamir215@gmail.com"

bot_name = 'GoT_Crawler'
datafile_path = "../data/got_crawler_data.csv"


def crawl(reddit, subreddit):
    """
    Crawls through a subreddits comments and writes them into the csv file using the reddit object provided.

    :param reddit: Reddit Instance of the bot
    :param subreddit: The subreddit to be crawled
    """

    data_file = reddit_helpers.open_file(datafile_path, 'a+')
    if data_file is False:
        return

    csv_writer = csv.writer(data_file)

    for comment in reddit.subreddit(subreddit).comments(limit=1000):
        csv_writer.writerow(
            [comment.id, comment.body, comment.score, comment.subreddit, comment.author, comment.created_utc])

    data_file.close()


def gather_data():
    """
    Main function that gathers the data for the three popular game of thrones subreddits
    """

    reddit = reddit_helpers.authenticate(bot_name)

    subreddits = ['gameofthrones', 'asoiaf', 'freefolk']

    for subreddit in subreddits:
        print("Reading from r/", subreddit, "...", sep="")
        crawl(reddit, subreddit)


if __name__ == "__main__":
    gather_data()
