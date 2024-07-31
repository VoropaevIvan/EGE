count = 0
with open('9.txt') as file:
    for s in file:
        a = [int(x) for x in s.split()]
        a_c = [a.count(x) for x in a]
        if (sorted(a) == a) + (a_c.count(3) == 3 and a_c.count(1) == 4) <= 1:
            count += 1
print(count)
