x = 3*3125**8 + 2*625**7 - 4*625**6 + 3*125**5 - 2*25**4 - 2024
base = 25
count = 0
while x != 0:
    last_d = x % base
    x = x // base
    if last_d == 0:
        count += 1
print(count)
