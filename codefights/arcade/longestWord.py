import re

def longestWord(text):
    alpha_only = re.split('[^a-zA-Z]', text)
    alpha_only.sort(key = len)

    return alpha_only[-1]