file = open('24.txt')
s = file.readline().strip()

ans = -1
c = 0
for i in range(len(s)):
    if c == 0 and s[i] == '0':
        continue
    if s[i] in '0123456789ABCDEF':
        c += 1
        ans = max(ans, c)
    else:
        c = 0
print(ans)

file.close()