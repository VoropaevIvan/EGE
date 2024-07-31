f = open('24-237.txt')
s = f.readline()
c = 2
otv = 0
for i in range(2, len(s)):
    if (s[i-2] in 'AE') and (s[i-1] in 'AE') and (s[i] in 'AE'):
        c = 2
    else:
        c += 1
        otv = max(otv, c)
print(otv)

