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

import collections
import sys
import string
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


def strip_punctuation(s):
    """Return the text without (hopefully...) any punctuation.
    >>> strip_punctuation('this.is?as!funny@word') == 'thisisasfunnyword'
    """
    return ''.join(ch for ch in s if ch not in string.punctuation)

freq = collections.Counter(sane_text)
for item in list(freq.most_common()):
    items = str(item)
    fitems = strip_punctuation(items)
    complete = fitems.split(" ")
    print(complete[0] + ": " + complete[1])
