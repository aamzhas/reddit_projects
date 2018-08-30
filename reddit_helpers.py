#!/usr/bin/env python

"""
File contains helper funtions for all Reddit Projects
"""

import praw

__author__ = "Aamir Hasan"
__version__ = "1.0"
__email__ = "hasanaamir215@gmail.com"


def authenticate(bot_name):
    """
    Authenticates a Reddit bot and returns as reddit instance

    :param bot_name: Name of the bot to be authenticated
    :return: Reddit instance of bot
    """

    print("Authenticating....")

    try:
        reddit = praw.Reddit(bot_name, user_agent=bot_name + " by u/Bangoes")
    except Exception as e:
        print("Authentication failed", str(e))
        return False

    print("Authenticated Successfully")
    return reddit


def read_from_file(path):
    """
    Reading from a file

    :param path: path to the file
    :return: Contents of the file
    """

    file_reader = open(path, "r")
    lines = file_reader.read().splitlines()
    file_reader.close()

    return lines


def write_to_file(path, lines):
    """
    Writes lines to a file

    :param path: path to the file
    :param lines: lines to be written
    """

    file_writer = open(path, "a+")

    for line in lines:
        file_writer.write(line + "\n")

    file_writer.close()
