"""Retrieve and print words from a URL.

Usage:

    python text_from_web.py <URL>
"""

import sys
from urllib.request import urlopen

def get_words(url):
    """Get a list of words from a URL.

    :param url: The URL of a UTF-8 text document.
    :returns A list of strings from the document.
    """
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)

def print_words(items):
    """Print items one per line.

    :param items: An iterable series of printable items.
    """
    for item in items:
        print(item)

def main(url):
    """Print each word from a text document from a URL

    :param url: The URL of a UTF-8 text document.
    """
    words = get_words(url)
    print_words(words)

if __name__ == '__main__':
    main(sys.argv[1]) #The 0th arg is the module filename