with open('24.txt') as file:
    s = file.readline().strip()

#s = 'RO_ROR____________________'
k = 21
l = 0
r = -1
count_RO = 0
ans = 0
while True:
    if count_RO <= k:
        r += 1
        if r == len(s):
            break
        if r - l + 1 >= 2:
            if s[r-1] + s[r] == 'RO':
                count_RO += 1
        if r - l + 1 >= 3:
            if s[r-2] + s[r-1] + s[r] == 'ROR':
                count_RO = 0
                l = r-1
                r = r
        if r - l + 1 >= 3:
            if s[r-2] + s[r-1] + s[r] == 'ORO':
                count_RO = 1
                l = r-1
                r = r
        if count_RO == k:
            ans = max(ans, r-l+1)
    else:
        l += 1
        if s[l-1] + s[l] == 'RO':
            count_RO -= 1
print(ans)
