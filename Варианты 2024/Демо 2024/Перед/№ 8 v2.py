from itertools import *

a = set(product('0234567', repeat=5))
count = 0
for x in a:
    s = ''.join(x)
    if s[0] != '0':
        if len(set(s)) == len(s):
            for d in '1357':
                s = s.replace(d, 'n')
            for d in '0246':
                s = s.replace(d, 'c')
            if ('nn' not in s) and ('cc' not in s):
                count += 1
print(count)
