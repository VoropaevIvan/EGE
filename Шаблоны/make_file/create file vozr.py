from random import *
with open('27-B.txt', 'w') as file:
    n = 10**6
    st = set()
    print(n, file=file)
    while len(st) != n:
        start = randint(0, 10**14)
        st.add(start)

    for x in sorted(st):
        print(x, file=file)

    st = set()
    while len(st) != n:
        start = randint(0, 10**14)
        st.add(start)

    for x in sorted(st):
        print(x, file=file)

