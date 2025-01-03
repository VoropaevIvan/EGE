with open('bI4DufyyF.txt') as file:
    s = file.readline().strip()
s = '**0-0---1*000*7-7-0-07-7'
s = s.replace('-', '*')
s = s.strip('*')

s = s.replace('**', ' ')
s = s.replace(' *', ' ')

s = s.replace('*0', ' ')

s = ' ' + s
while ' 0' in s:
    s = s.replace(' 0', ' ')
s = s.replace(' *', ' ')

ans = -1
for x in s.split():
    if '*' in x:
        print(x)
        ans = max(ans, len(x))
print(ans)