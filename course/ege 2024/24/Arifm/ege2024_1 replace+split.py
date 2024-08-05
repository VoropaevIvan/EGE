with open('ege2024_1.txt') as file:
    s = file.readline().strip()

#s = '***77*07*77*70000*0001'
#s = '1*0*1'
s = ' ' + s + ' '
s = s.replace('-', '*')
while s[0] == '*':
    s = s[1:]
while s[-1] == '*':
    s = s[:-1]
# s = s.strip('+')
s = s.replace('*0', ' ')
while ' 0' in s:
    s = s.replace(' 0', ' ')
while '* ' in s:
    s = s.replace('* ', ' ')

s = s.replace('**', ' ')
s = s.replace(' *', ' ')
#print(s)
ans = -1
for x in s.split():
    if '*' in x:
        #print(x)
        ans = max(ans, len(x))
print(ans)
