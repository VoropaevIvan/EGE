def delit(x):
    st = set()
    for d in range(1, int(x**0.5)+1):
        if x % d == 0:
            st.add(d)
            st.add(x // d)
    return sorted(st)

for x in range(123456, 987654+1):
    delitely = delit(x)
    if len(delitely) == 5:
        print(delitely[-2], delitely[-1])


