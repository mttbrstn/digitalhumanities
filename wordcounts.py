#!/usr/bin/env python
"""
wordcounts.py:

A first attempt at a digital humanities project. This program will take
a text file, convert the words to lowercase, remove punctuation, and
return a list of words ordered by the frequency of their use.

Run the file from your *nix command line with the plain text filename as
your argument.

Version 1.0
Matt Burstein

"""

import re
import collections
import sys
# from pprint import pprint


def sanitize_text(text):
    punctuation = '!@#$%^&*()_-+={}[]:;"\'|<>,.?/~`'
    for marker in punctuation:
        for item in text:
            item.replace(marker, "")
    return text

number_of_hits = 0

file = sys.argv[1]
f = open(file, 'r')
ftext = f.read()
f.close()

words = ftext.split()

lcwords = []
for item in words:
    lcwords.append(item.lower())

sane_text = sanitize_text(lcwords)

freq = collections.Counter(sane_text)
for item in list(freq.most_common()):
    items = str(item)
    fitems = items.strip('\"\'()[]" ')
    clean = re.sub('\.|\'|;|:', '', fitems)
    print(re.sub(',', ':', clean))
