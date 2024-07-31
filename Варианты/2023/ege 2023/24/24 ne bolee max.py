with open('308_24.txt') as file:
    s = file.readline().strip()

l, r = 0, -1
count_W = 0
ans = -1
while True:
    if count_W <= 130:
        r += 1
        if r == len(s):
            break
        if s[r] == 'W':
            count_W += 1
    else:
        l += 1
        if s[l-1] == 'W':
            count_W -= 1
    if count_W <= 130:
        ans = max(ans, r-l+1)
print(ans)