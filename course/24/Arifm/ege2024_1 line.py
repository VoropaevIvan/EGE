with open('ege2024_1.txt') as file:
    s = file.readline().strip()

s = s.replace('-', '*')
s = '**' + s + '**'
start = 0
is_plus_in = 0
ans = -1
for i in range(1, len(s)):
    if s[i] == '*':
        if s[i-1] == '*' or start == i:
            start = i+1
            is_plus_in = 0
        else:
            is_plus_in = 1
    else:
        if s[i] == '0':
            if (is_plus_in and s[i-1] == '*') or start == i:
                start = i+1
                is_plus_in = 0
        if is_plus_in:
            ans = max(ans, i - start + 1)
            #print(s[start:i + 1])
print(ans)