f = open('24.txt')
s = f.readline()
c = 1
otv = 0
for i in range(1, len(s)):
    if (s[i-1] in 'NPO') and (s[i] in 'NPO'):
        c = 1
    else:
        c += 1
        otv = max(otv, c)
print(otv)

