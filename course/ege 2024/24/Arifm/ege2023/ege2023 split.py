with open('ege2023.txt') as file:
    s = file.readline().strip()
#s = '1+2++++2'
a = s.split('+')
ans = -1
cur_s = ''
cur_count = 0
for i in range(len(a)):
    if a[i] != '':
        if cur_s == '':
            cur_s = a[i]
        else:
            cur_s = cur_s + '+' + a[i]
        cur_count += 1
        if cur_count >= 2:
            ans = max(ans, len(cur_s))
    else:
        cur_s = ''
        cur_count = 0
print(ans)
