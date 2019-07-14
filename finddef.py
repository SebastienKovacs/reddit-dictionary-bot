#!/usr/bin/python3
import json
from formatdef import formatdef


def definition(word):
	with open('dictionary/dictionary.json') as json_file:  
		data = json.load(json_file)
		try:
			return formatdef((data[word.lower()]))
		except:
			return "Sorry, i couldn't find the definition for " + word + "."
