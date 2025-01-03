import random


def generate_s(len_):
    symbols = '+*0789'
    start = 0
    end = len(symbols) - 1
    s = ''
    for i in range(len_):
        r = random.randint(start, end)
        s += symbols[r]
    return s
