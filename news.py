from __future__ import print_function
from collections import defaultdict
import os
import random

print('Loading function')


def handler(event, context):
    heads_path = os.environ['LAMBDA_TASK_ROOT'] + "/heads"
    words_path = os.environ['LAMBDA_TASK_ROOT'] + "/words"
    with open(heads_path) as f:
        heads = f.readlines()
        f.close()
    with open(words_path) as f:
        words = f.readlines()
        f.close()

    word_list = defaultdict(list)
    for word in words:
        elem = word.split('\t')
        word_list[elem[1].rstrip()].append(elem[0].rstrip())

    head_template = heads[random.randint(0, len(heads)-1)]
    news = ""

    for word in head_template.split():
        if word[:1] == '[':
            new_word_list = word_list[word[1:]]
            new_word = new_word_list[random.randint(0, len(new_word_list)-1)]
            news = news + new_word + " "
        else:
            news = news + word + " "

    html_output = '<HTML><BODY><B>' + news.upper() + '</B></BODY></HTML>'
    return html_output

if __name__ == "__main__":
    testOut = handler("a", "b")
    print(testOut)
