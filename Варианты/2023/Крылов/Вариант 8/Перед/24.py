with open('24var08.txt') as file:
    s = file.readline().strip()

l, r = 0, -1
count_AB = 0
ans = -1
while True:
    if count_AB <= 21:
        r += 1
        if r == len(s):
            break
        if r-l+1 >= 2 and s[r-1] + s[r] == 'AB':
            count_AB += 1
    else:
        l += 1
        if s[l-1] + s[l] == 'AB':
            count_AB -= 1
    if count_AB == 21:
        ans = max(ans, r-l+1)
print(ans)