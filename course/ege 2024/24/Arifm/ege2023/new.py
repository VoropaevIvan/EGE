# line 2
with open('ege2023.txt') as file:
    s = file.readline().strip()

s = s.strip('+')
t = s[0]
is_plus_in = 0
ans = -1
for i in range(1, len(s)):
    t += s[i]
    if s[i] in '123456789':
        if is_plus_in:
            ans = max(ans, len(t))
            print(t)
    else:
        is_plus_in = 1
        if s[i - 1] == '+':
            t = ''
            is_plus_in = 0
print(ans)