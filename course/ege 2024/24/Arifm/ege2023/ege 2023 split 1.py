with open('ege2023.txt') as file:
    s = file.readline().strip()
s = '++68+12+1++2+1+++3++4+5+'
while s[0] == '+':
    s = s[1:]
while s[-1] == '+':
    s = s[:-1]
# s = s.strip('+')

s = s.replace('++', ' ')
s = s.replace(' +', ' ')

ans = -1
for x in s.split():
    if '+' in x:
        print(x)
        ans = max(ans, len(x))
print(ans)

# ++1+2++3+++4+6+8+++
#
# 1+2++3+++4+6+8
# 1+2 3 +4+6+8
# 1+2 3 4+6+8