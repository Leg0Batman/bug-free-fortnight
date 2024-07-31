import os
import praw
import config




def bot_login():
    r =praw.Reddit(username=config.username,
            password=config.password,
            client_id=config.client_id,
            client_secret=config.client_secret,
            user_agent="N0T a B0T223's test comment responder v0.1")
    return r

def run_bot(r, comments_replied_to):
    for comment in r.subreddit('test').comments(limit=10):
        if comment.id not in comments_replied_to and comment.author != r.user.me():
            if "Lebron" in comment.body:
                print("String with \"Lebron\" found in comment with comment ID: " + comment.id)
                comment.reply("I also love Lebron! [Here] https://i.imgur.com/2hBebTU.jpeg is an image of him")
                comments_replied_to.append(comment.id)
                with open("comments_replied_to.txt", "a") as f:
                    f.write(comment.id + "\n")

def get_saved_comments():
    if not os.path.isfile("comments_replied_to.txt"):
        comments_replied_to = []
    else:
        with open("comments_replied_to.txt", "r") as f:
            comments_replied_to = f.read()
            comments_replied_to = comments_replied_to.split("\n")
        return comments_replied_to
    

r = bot_login()
comments_replied_to = get_saved_comments()  

while True:
    run_bot(r,comments_replied_to)