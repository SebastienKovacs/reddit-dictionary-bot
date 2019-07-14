# reddit-dictionary-bot

This is a simple bot that identifies questions in this format: "what does [word] mean?".
The bot then replies with the definition of the given word according to the dictionary in dictionary/dictionary.json.
I didn't put any dictionary there on purpose because these kind of files are huge but any json file with word definitions should 
work as long as the words in it are all in lowercase.

The script has almost no dependencies as json, time, re, and sys should be included with a standard python3 install.
The only dependency that should be downloaded is the reddit client API: praw.
