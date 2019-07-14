#!/usr/bin/python3
def remember_comment(comment):
	with open('oldcomments.txt', 'a') as filehandle:
		filehandle.writelines("%s\n" % place for place in comment)



def read_comment_list():
	with open('oldcomments.txt', 'r') as filehandle:
		filecontents = filehandle.readlines()

		oldcomments = []
		for line in filecontents:
			oldcomment = line[:-1]
			oldcomments.append(oldcomment)

		return oldcomments



def is_new(comment):
	oldcomments = read_comment_list()
	for oldcomment in oldcomments:
		if str(comment) == oldcomment:
			return False

	return True