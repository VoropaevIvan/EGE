with open('24_11630.txt') as file:
    s = file.readline().strip()

ans = -1
for i in range(len(s)):
    plus_in = 0
    if s[i] != '+':
        for j in range(i+1, len(s)):
            if s[j-1]+ s[j] == '++':
                break
            if s[j] !='+' and plus_in:
                ans = max(ans, j - i + 1)
            if s[j] == '+':
                plus_in = 1
    print(i, ans)
print(ans)