'''
Created on Dec 23, 2015

@author: preston wilson
'''

import praw
import time

r = praw.Reddit(user_agent = "test_version 1.0")

f = file("information.txt", "r")
fileName = f.readline()
filePass = f.readline()
r.login(fileName, filePass, disable_warning=True)

print("sucessfully logged in!")

words_to_match = ['5/7']
already = [] #contains every comment already replied to

def run_bot():
    print("searching...")
    subreddit = r.get_subreddit("pics")
    comments = subreddit.get_comments(limit = 100)
    for every in comments:
        comment = every.body.lower()
        contains = any(string in comment for string in words_to_match)
        
        if every.id not in already and contains:
            every.reply("5/7, perfect! \nWell memed my friend!")
            already.append(every.id)
            print("found a 5/7")
            
            
while True:
    run_bot()
    time.sleep(2)           
        