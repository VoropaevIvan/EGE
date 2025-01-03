import re

with open('mG-kU8F-l.txt') as file:
    s = file.readline().strip()
print(len(s))

ans = -1
#s = 'AAZZZAA'
regex_obj = re.compile('(?:[^Z]*Z[^Z]*){200}')
for i in range(len(s)):
    res = re.match(regex_obj, s[i:])
    #print(res)
    print(i)
#ans = max(res, key=len)
#print(len(ans))
#print(ans)
print(res)