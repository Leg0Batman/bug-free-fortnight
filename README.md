Project: Reddit Bot
Function: Scans the 25 most recent comments in the 'test' subreddit for the string "Lebron" and replies to matching comments.
How it works:
Uses the Python Reddit API Wrapper (PRAW) to interact with Reddit's API.
Logs into Reddit using credentials stored in a separate config.py file.
Fetches the 25 most recent comments from the 'test' subreddit.
Checks each comment for the string "Lebron" and ensures the comment's author is not the bot itself.
If both conditions are met, the bot replies to the comment.
Keeps track of which comments it has replied to by storing their IDs in a file named comments_replied_to.txt.
Setup:
Clone the repository.
Install the required Python packages.
Create a config.py file with your Reddit credentials.
Run the bot with python reddit_bot.py.
License: MIT License