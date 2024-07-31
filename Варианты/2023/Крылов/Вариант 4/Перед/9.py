count = 0
with open('9.txt') as file:
    for s in file:
        a = [int(x) for x in s.split()]
        a_c = [a.count(x) for x in a]
        if a_c.count(4) == 4 and a_c.count(2) == 2 and a_c.count(1) == 2:
            a_n = [a[i] for i in range(8) if a_c[i] == 1]
            a_p = [a[i] for i in range(8) if a_c[i] > 1]
            if sum(a_n) / len(a_n) >= max(a_p):
                count += 1
print(count)