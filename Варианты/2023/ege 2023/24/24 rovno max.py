with open('301_24.txt') as file:
    s = file.readline().strip()

l, r = 0, -1
count_T = 0
ans = -1
while True:
    if count_T <= 100:
        r += 1
        if r == len(s):
            break
        if s[r] == 'T':
            count_T += 1
    else:
        l += 1
        if s[l-1] == 'T':
            count_T -= 1
    if count_T == 100:
        ans = max(ans, r-l+1)
print(ans)