count = 0
with open('9.txt') as file:
    for s in file:
        a = [int(x) for x in s.split()]
        a_c = [a.count(x) for x in a]
        a_p = [a[i] for i in range(8) if a_c[i] > 1]
        if a_c.count(2) == 6 and a_c.count(1) == 2:
            if min(a) not in a_p:
                count += 1
print(count)