with open('24.txt') as file:
    s = file.readline().strip()

ans = -1
c = 0
s = '!' + s
for i in range(len(s)):
    if s[i] in 'VWXYZ':
        if s[i-1] + s[i] in 'ZVWXYZ':
            c += 1
        else:
            c = 1
    else:
        c = 0
    ans = max(ans, c)
print(ans)