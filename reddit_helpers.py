#!/usr/bin/env python

"""
File contains helper funtions for all Reddit Projects
"""

import os

import praw

__author__ = "Aamir Hasan"
__version__ = "1.0.1"
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


def open_file(path, permission):
    if os.path.exists(path):
        return open(path, permission)

    print("Path does not exist!")
    return False

def read_from_file(path):
    """
    Reading from a file

    :param path: path to the file
    :return: Contents of the file
    """

    file = open_file(path, "r")

    if file is False:
        return ""

    lines = file.read().splitlines()
    file.close()

    return lines


def write_to_file(path, lines):
    """
    Writes lines to a file

    :param path: path to the file
    :param lines: lines to be written
    """

    file = open_file(path, "a+")

    if file is False:
        return

    for line in lines:
        file.write(line + "\n")

    file.close()
