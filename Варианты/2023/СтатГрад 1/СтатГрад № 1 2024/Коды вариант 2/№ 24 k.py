file = open('24.txt')
s = file.readline().strip()

l, r = 0, -1
count_X, count_Y = 0, 0
ans = -1
while True:
    if count_X > 1 or count_Y > 1:
        l += 1
        if s[l-1] == 'X':
            count_X -= 1
        if s[l-1] == 'Y':
            count_Y -= 1
    else:
        r += 1
        if r == len(s):
            break
        if s[r] == 'X':
            count_X += 1
        if s[r] == 'Y':
            count_Y += 1
    if count_X == 1 and count_Y == 1:
        ans = max(ans, r - l + 1)
print(ans)