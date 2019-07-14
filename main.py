#!/usr/bin/python3
import praw
import time
from regextests import regex
import oldcomments


def make_reply(regexList):
	reply = "Here is the webster definition for " + regexList[0] + ":\n\n"
	reply += regexList[1]
	return reply



def reply_the_def(comment):
	isReplied = False
	reply = make_reply(regex(comment.body))

	while not isReplied:
		try:
			comment.reply(reply)
			isReplied = True
		except:
			print("Waiting to be allowed to comment again.")
			time.sleep(60)

	oldcomments.remember_comment([comment])



def parse_comments(comments):
	comments.replace_more(limit = None)

	for comment in comments.list():
		print(comment)
		if regex(comment.body) and oldcomments.is_new(comment):
			reply_the_def(comment)



def main():
	reddit = praw.Reddit(client_id = "dnWTa_zmtie4XQ",
		client_secret = "b-xYSCyq7WzOeweLHqcPjAa3WL0",
		user_agent = "definitionbot",
		username = "webster_def_bot",
		password = "Sebkov1508")

	subreddit = reddit.subreddit("testabot")

	while True:
		new = subreddit.new(limit = 5)
		
		for submission in new:
			print("\n", submission.title, "\n")
			parse_comments(submission.comments)

		time.sleep(30)


if __name__=="__main__":
	main()