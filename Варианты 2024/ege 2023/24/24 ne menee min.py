with open('331_24.txt') as file:
    s = file.readline().strip()

l, r = 0, -1
count_Y = 0
ans = 10**10
while True:
    if count_Y < 260:
        r += 1
        if r == len(s):
            break
        if s[r] == 'Y':
            count_Y += 1
    else:
        l += 1
        if s[l-1] == 'Y':
            count_Y -= 1
    if count_Y >= 260:
        ans = min(ans, r-l+1)
print(ans)