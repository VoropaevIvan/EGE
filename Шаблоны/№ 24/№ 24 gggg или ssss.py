f = open('24-237.txt')
s = f.readline()
c = 1
otv = 0
for i in range(1, len(s)):
    if (s[i-1] in 'AE') != (s[i] in 'AE'):
        c = 1
    else:
        c += 1
        otv = max(otv, c)
print(otv)

