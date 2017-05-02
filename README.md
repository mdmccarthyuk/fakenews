# fakenews
### Generate fake news from a set of headline templates and word lists.

A lambda function test.

The words file contains a tab delimited list of words and categories
The heads file contains a list of headline templates used to build the fake news.

The script reads a word at a time from a randomly selected headline in the heads file.  
If a word is found to start with a '[' symbol the word is looked up in the words file and matched on a random word with
the category given after the '['.  
