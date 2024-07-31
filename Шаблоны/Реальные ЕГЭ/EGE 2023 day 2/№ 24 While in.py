f = open('24.txt')
s = f.readline().strip()
for x in '123456789ABCDEF':
    s = s.replace(x, '*')

otv = ''
while otv + '*' in s:
    otv = otv + '*'

print(len(otv))

f.close()