with open('301_24.txt') as file:
    s = file.readline().strip()

l, r = 0, -1
count_X = 0
ans = -1
while True:
    if count_X <= 1000:
        r += 1
        if r == len(s):
            break
        if s[r] == 'X':
            count_X += 1
    else:
        l += 1
        if s[l-1] == 'X':
            count_X -= 1
    if count_X == 1000:
        ans = max(ans, r-l+1)
print(ans)