import random


def generate(len_, start, end):
    a = []
    for i in range(len_):
        r = random.randint(start, end)
        a.append(r)
    return (a, len_)
