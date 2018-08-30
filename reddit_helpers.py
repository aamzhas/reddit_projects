import praw

# authenticating and getting a reddit instance
def authenticate():
    print("Authenticating....")

    reddit = praw.Reddit('GoT_Crawler', user_agent='Comment Extraction by /u/Bangoes')

    print("Authenticated Successfully")
    return reddit

def read_from_file(path, filename):
    file_reader = open(path + filename, "r")
    seen_comments = file_reader.read().splitlines()
    file_reader.close()

    return seen_comments


def write_to_file(path, filename, new_comments):
    file_writer = open(path + filename, "a+")
    for id in new_comments:
        file_writer.write(id + "\n")
    file_writer.close()
