with open('319_24.txt') as file:
    s = file.readline().strip()

l, r = 0, -1
count_Z = 0
ans = 10**10
while True:
    if count_Z < 200:
        r += 1
        if r == len(s):
            break
        if s[r] == 'Z':
            count_Z += 1
    else:
        l += 1
        if s[l-1] == 'Z':
            count_Z -= 1
    if count_Z == 200:
        ans = min(ans, r-l+1)
print(ans)