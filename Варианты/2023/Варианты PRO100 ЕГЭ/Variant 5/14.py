a = 3*3125**9 + 2*625**8 - 4*625**7 +3*125**6 - 2*25**5 - 2024
count_0 = 0

while a != 0:
    last_d = a % 25
    if last_d == 0:
        count_0 += 1
    a //= 25
print(count_0)



