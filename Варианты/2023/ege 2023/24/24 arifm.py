with open('24_11630.txt') as file:
    s = file.readline().strip()


ans = -1
ok_start = 0
plus_in = 0
c = 0
for i in range(len(s)):
    if c > 0:
        if s[i-1]+ s[i] != '++':
            c += 1
        else:
            c = 0
            ok_start = 0
            plus_in = 0
            continue
        if s[i] != '+':
            if plus_in:
                ans = max(ans, c)
        else:
            plus_in = 1
    elif c == 0:
        if s[i] != '+':
            c += 1
            if plus_in:
                ans = max(ans, c)
print(ans)

