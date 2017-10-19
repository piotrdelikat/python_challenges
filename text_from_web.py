#get text as strings from txt file at URL
import sys
from urllib.request import urlopen

def get_words(url):
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)

def print_words(items):
    for item in items:
        print(item)

def main(url):
    words = get_words(url)
    print_words(words)

if __name__ == '__main__':
    main(sys.argv[1])