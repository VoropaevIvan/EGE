x = 343**1515 - 6*49**1520 + 5*49**1510 - 3*7**1530 - 1550
base = 7
count = 0
while x != 0:
    last_d = x % base
    x = x // base
    if last_d == 0:
        count += 1
print(count)
