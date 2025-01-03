with open('24.txt') as file:
    s = file.readline().strip()

ans = -1
c = 0
for i in range(len(s)):
    if s[i] in '123456789ABCDEF':
        c += 1
        ans = max(ans, c)
    else:
        c = 0
print(ans)