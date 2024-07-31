file = open('24_2024.txt')
s = file.readline().strip()
l = 0
count_T = 0
ans = -1
for r in range(0, len(s)):
    if s[r] == 'T':
        count_T += 1
    if count_T <= 100:
        if count_T == 100:
            an


