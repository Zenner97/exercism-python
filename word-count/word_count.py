
import re


def word_count(string):

    line = string.replace('_', ' ').lower()
    pattern = re.findall("[\w']+", line)
    count = {}
    for word in pattern:
        count[word] = 1
        if count[word] != word in pattern:
            count[word] += 1
    return count
#    return {word: pattern.count(word) for word in pattern}
