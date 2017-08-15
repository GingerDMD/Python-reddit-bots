'''
Created on Dec 23, 2015

@author: preston wilson
'''

import praw
import time

r = praw.Reddit(user_agent = "Shirley 1.0")

f = open("information_shirley.txt", "r")
fileName = f.readline()
filePass = f.readline()
r.login(fileName, filePass, disable_warning=True)

print("successfully logged in!")

words_to_match = ['surely']
already = []


def run_bot():
    # print("searching...")
    subreddit = r.get_subreddit("all")
    comments = subreddit.get_comments(limit = 100)
    for every in comments:
        comment = every.body.lower()
        contains = any(string in comment for string in words_to_match)
        if every.id not in already and contains:
            every.reply("Don't call me Shirley, pal!")
            already.append(every.id)
            print("found a shirley")
            time.sleep(600)


def run():
    while True:
        run_bot()
        time.sleep(2)


def hourToSec(hours):
    seconds = 0
    try:
        seconds = int(hours) * 60 * 60
        return seconds
    except SyntaxError:
        print("error of some sort")


while True:
    run()
    time.sleep(hourToSec(4))
    print('time is: ' + time.localtime())


