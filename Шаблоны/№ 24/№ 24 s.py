f = open('24-257.txt')
s = f.readline()[:1000000]
c = 0
for i in range(1, len(s)):
    c += (('A'*i) in s)


print(c)

