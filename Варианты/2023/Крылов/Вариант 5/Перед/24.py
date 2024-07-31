with open('24var05.txt') as file:
    s = file.readline().strip()

l, r = 0, -1
count_A = 0
ans = -1
while True:
    if count_A <= 3:
        r += 1
        if r == len(s):
            break
        if s[r] == 'A':
            count_A += 1
    else:
        l += 1
        if s[l-1] == 'A':
            count_A -= 1
    if count_A <= 3:
        ans = max(ans, r-l+1)
print(ans)