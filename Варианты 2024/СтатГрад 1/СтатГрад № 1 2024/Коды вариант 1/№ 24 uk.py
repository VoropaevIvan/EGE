file = open('24.txt')
s = file.readline().strip()

l, r = 0, -1
count_A, count_B = 0, 0
ans = -1
while True:
    if count_A > 1 or count_B > 1:
        l += 1
        if s[l-1] == 'A':
            count_A -= 1
        if s[l-1] == 'B':
            count_B -= 1
    else:
        r += 1
        if r == len(s):
            break
        if s[r] == 'A':
            count_A += 1
        if s[r] == 'B':
            count_B += 1
    if count_A == 1 and count_B == 1:
        ans = max(ans, r - l + 1)
print(ans)