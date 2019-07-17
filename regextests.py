#!/usr/bin/python3
import re
import sys
from finddef import definition


def regex(question):

	matchObj = re.match( r'what does (.*) mean', question, re.M|re.I)

	if matchObj:
		return [matchObj.group(1), definition(matchObj.group(1))] 
	else:
		return None