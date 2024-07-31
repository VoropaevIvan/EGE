with open('24var09-12.txt') as file:
    s = file.readline().strip()

count = 1
ans = -1
for i in range(1, len(s)):
    if s[i-1] + s[i] == '00':
        count = 1
    else:
        count += 1
    ans = max(ans, count)
print(ans)