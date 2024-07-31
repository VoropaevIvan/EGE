with open('24 (15).txt') as file:
    s = file.readline().strip()

l, r = 0, -1
count_Y = 0
ans = -1
while True:
    if count_Y <= 150:
        ans = max(ans, r - l + 1)
        r += 1
        if r == len(s):
            break
        if s[r] == 'Y':
            count_Y += 1
    else:
        l += 1
        if s[l-1] == 'Y':
            count_Y -= 1
print(ans)
# Решение № 24 из ЕГЭ 2023 от PRO100 ЕГЭ



