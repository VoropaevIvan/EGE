balance = [0] * 1442
with open('26_r.txt') as file:
    N = int(file.readline())
    for s in file:
        start, end = [int(x) for x in s.split()]
        for minute in range(start, end):
            balance[minute] += 1
print(balance)
pik = max(balance)
count_piks = 0
for minute in range(0, 1440):
    if balance[minute - 1] != pik and balance[minute] == pik:
        count_piks += 1
print(count_piks, pik)
