import re
from collections import Counter


def mostCommonWord(paragraph: str, banned) -> str:
    """
    :type paragraph: str
    :type banned: List[str]
    :rtype: str
    """
    # switch to lowercase
    paragraph = paragraph.lower()
    # remove punctuations and convert to list
    paragraph = re.sub("[^a-zA-Z and ^" "]", " ", paragraph)
    # split by words and convert to list
    paragraph = list(paragraph.split())
    # count by frequency
    counter = list(Counter(paragraph).most_common())
    # print(counter)
    # remove banned
    for word in counter:
        if word[0] in banned:
            continue
        else:
            return word[0]

par = "a, a, a, a, b,b,b,c, c"
ban = ["a"]
print(mostCommonWord(par, ban))
