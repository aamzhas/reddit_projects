import csv
import reddit_helpers

# path where
path = "./files/"
comment_ids_filename = "comments_seen.txt"
data_filename = "data.csv"

# crawl the given subreddit
def crawl(reddit, subreddit):
    data_file = open(path + data_filename, 'a+')
    csv_writer = csv.writer(data_file)

    for comment in reddit.subreddit(subreddit).comments(limit=999999999999):
        csv_writer.writerow([comment.id, comment.body, comment.score, comment.subreddit, comment.created])

    data_file.close()

def gather_data():
    reddit = reddit_helpers.authenticate()
    subreddits = ['gameofthrones', 'asoiaf', 'freefolk']
    for subreddit in subreddits:
        crawl(reddit, subreddit)

if __name__ == "__main__":
    gather_data()
