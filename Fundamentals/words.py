#!/usr/bin/env python3
"""Retrive and print words from a URL

Usage:
    python words.py <URL>
"""

import sys
from urllib.request import urlopen

def fetch_words(url):
    """Fetch a list of words from a URL.

    Args:
        url: The URL of a UTF-8 text document.
        
    Returns:
        A list of string containing the words from 
        the document.
    """
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    return story_words


def print_items(items):
    """So I can write wherever i want here
    and it is going to apper at the terminal.

    I all have to do is write the following:
    
    from words import *
    Help(print_items)
    """
    for item in items:
        print(item)


def main(url):    
    """
        Here I will have more data.

        this prints wach word from the text downloaded by the url
    """
    words = fetch_words(url) 
    print_items(words)


if __name__ == '__main__':
    main(sys.argv[1]) #the argv[1] is because the index 0 is the module filename