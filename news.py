from __future__ import print_function
from collections import defaultdict

import json
import os
import random

print('Loading function')


def handler(event, context):
    configPath = os.environ['LAMBDA_TASK_ROOT']
    headsPath = os.environ['LAMBDA_TASK_ROOT'] + "/heads"
    wordsPath = os.environ['LAMBDA_TASK_ROOT'] + "/words"
    with open(headsPath) as f:
        heads = f.readlines()
        f.close()
    with open(wordsPath) as f:
        words = f.readlines()
        f.close()

    wordList = defaultdict(list)
    for word in words:
        elem = word.split('\t')
        wordList[elem[1].rstrip()].append(elem[0].rstrip())

    headTemplate = heads[random.randint(0,len(heads)-1)]
    news = ""

    for word in headTemplate.split():
        if word[:1] == '[':
            newWordList = wordList[word[1:]]
            newWord = newWordList[random.randint(0,len(newWordList)-1)]
            news = news + newWord + " "
        else:
            news = news + word + " "

    htmlOutput = '<HTML><BODY><B>' + news.upper() + '</B></BODY></HTML>'
    print(htmlOutput)
    return htmlOutput

if __name__ == "__main__":
    handler("a","b")
