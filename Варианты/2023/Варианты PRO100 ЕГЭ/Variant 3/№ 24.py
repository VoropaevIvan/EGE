with open('24.txt') as file:
    s = file.readline().strip()

l, r = 0, -1
count_X = 0
ans = 10**10
while True:
    if s[r] == 'Y':
        l = r+1
        r = r
        count_X = 0
    if count_X >= 500:
        ans = min(ans, r-l+1)
        l += 1
        if s[l-1] == 'X':
            count_X -= 1
    else:
        r += 1
        if r == len(s):
            break
        if s[r] == 'X':
            count_X += 1
print(ans)

