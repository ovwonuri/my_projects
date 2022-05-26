# Read text from a file, and count the occurrence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}
import re
from collections import Counter


def read_file_content(filename):
    # [assignment] Add your code here
    with open(filename) as f:
        contents = f.read()
        return contents


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    # using regex (findall())
    # to count words in string
    words = re.findall(r'\w+', text)
    return Counter(words)


print(count_words())
