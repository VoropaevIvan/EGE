count = 0
with open('files/9.txt') as file:
    for s in file:
        a = [int(x) for x in s.split()]
        a_c = [a.count(x) for x in a]
        a_n = [x for x in a if a.count(x) == 1]
        a_p = [x for x in a if a.count(x) > 1]
        if max(a_c) >= 3:
            if 1 in a_c:
                if sum(a_p)/len(a_p) > sum(a_n)/len(a_n):
                    count += 1
print(count)