with open('24.txt') as file:
    s = file.readline().strip()

ans = -1
for i in range(len(s)):
    for j in range(i, len(s)):
        t = s[i:j+1]
        if 'ORO' not in t and 'ROR' not in t:
            if t.count('RO') == 21:
                ans = max(ans, j-i+1)
print(ans)