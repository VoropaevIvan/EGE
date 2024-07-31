with open('24_17616.txt') as file:
    s = file.readline().strip()

for x in '23456789':
    s = s.replace(x, '1')

max_len = -1
cur_len = 0
ans = ''

spl_p = s.split('+')
for i in range(len(spl_p)):
    print(i)
    spl_m = spl_p[i].split('*')
    if ('0' in spl_m) and ('' not in spl_m):
        cur_len += len(spl_p[i])
        ans = ans + '+' + spl_p[i]
        #print(spl_m)
        max_len = max(max_len, cur_len)
    else:
        cur_len = 0
print(max_len)




