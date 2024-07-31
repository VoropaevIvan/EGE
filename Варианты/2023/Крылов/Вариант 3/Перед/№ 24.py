with open('24var03.txt') as file:
    s = file.readline().strip()

l, r = 0, -1
count_A = 0
ans = 10**10
while True:
    if count_A < 500:
        r += 1
        if r == len(s):
            break
        if s[r] == 'A':
            count_A += 1
    else:
        l += 1
        if s[l-1] == 'A':
            count_A -= 1
    if count_A >= 500:
        ans = min(ans, r-l+1)
print(ans)