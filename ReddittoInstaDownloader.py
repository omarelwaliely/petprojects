import urllib
import os
import praw
from instabot import Bot
import schedule
import time


def download():
    reddit = praw.Reddit(client_id="",
                         username="", password="", user_agent="l")
    subreddit = reddit.subreddit("")
    count = 0

    for submission in subreddit.hot(limit=None):
        url = str(submission.url)
        if url.endswith("jpg") or url.endswith("jpeg") or url.endswith("png"):
            urllib.request.urlretrieve(url, os.path.join(
                "directory", f"image{count}.jpg"))
            if count == 0:
                caption1 = str(submission.title)
            elif count == 1:
                caption2 = str(submission.title)
            elif count == 2:
                caption3 = str(submission.title)
            count += 1
            if count == 3:
                break
    subreddit = reddit.subreddit("")
    count = 0
    for submission in subreddit.hot(limit=None):
        url = str(submission.url)
        if url.endswith("jpg") or url.endswith("jpeg") or url.endswith("png"):
            urllib.request.urlretrieve(url, os.path.join(
                "directory", f"image{4}.jpg"))
            if count == 0:
                caption5 = str(submission.title)
            count += 1
            if count == 1:
                break
    subreddit = reddit.subreddit("")
    count = 0
    for submission in subreddit.hot(limit=None):
        url = str(submission.url)
        if url.endswith("jpg") or url.endswith("jpeg") or url.endswith("png"):
            urllib.request.urlretrieve(url, os.path.join(
                "directory", f"image{3}.jpg"))
            if count == 0:
                caption4 = str(submission.title)
            count += 1
            if count == 1:
                break
    subreddit = reddit.subreddit("")
    count = 0
    for submission in subreddit.hot(limit=None):
        url = str(submission.url)
        if url.endswith("jpg") or url.endswith("jpeg") or url.endswith("png"):
            urllib.request.urlretrieve(url, os.path.join(
                "directory", f"image{5}.jpg"))
            if count == 0:
                caption6 = str(submission.title)
            count += 1
            if count == 1:
                break
    bot = Bot()

    def twooclock():
        bot.login(username="", password="")
        file = "directory/image0.jpg"
        bot.upload_photo(file, caption=f"{caption1}custom caption here")
        bot.logout()

    def fiveoclock():
        bot.login(username="", password="")
        file = "directory/image1.jpg"
        bot.upload_photo(file, caption=f"{caption2}custom caption here")
        bot.logout()
        bot.login(username="", password="")
        file = "directory/image4.jpg"
        bot.upload_photo(file, caption=f"{caption5}custom caption here")
        bot.logout()

    def eightoclock():
        bot.login(username="", password="")
        file = "directory/image2.jpg"
        bot.upload_photo(file, caption=f"{caption3}custom caption here")
        file = "directory/image5.jpg"
        bot.upload_photo(file, caption=f"{caption6}custom caption here")
        bot.logout()

    schedule.every().day.at("14:20").do(twooclock)
    schedule.every().day.at("17:20").do(fiveoclock)
    schedule.every().day.at("20:20").do(eightoclock)
    while True:
        schedule.run_pending()
        time.sleep(1)


download()
