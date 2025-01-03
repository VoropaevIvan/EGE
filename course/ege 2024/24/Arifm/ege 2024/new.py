# line 2
with open('bI4DufyyF.txt') as file:
    s = file.readline().strip()

s = s.replace('-', '*')
s = s.rstrip('*')
s = s.lstrip('*0')

t = s[0]
is_plus_in = 0
ans = -1
for i in range(1, len(s)):
    t += s[i]
    if s[i] in '0123456789':
        if t[-2:] == '*0' or t == '0':
            t = ''
            is_plus_in = 0
        if is_plus_in:
            ans = max(ans, len(t))
            print(t)
    else:
        is_plus_in = 1
        if s[i - 1] == '*' or t == '*':
            t = ''
            is_plus_in = 0
print(ans)