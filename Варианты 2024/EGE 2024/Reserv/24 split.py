def check(s):
    split_mult = s.split('*')
    return ('0' in split_mult) and ('' not in split_mult) and all(x[:2] not in ['00', '01'] for x in split_mult)


with open('24_17641.txt') as file:
    s = file.readline().strip()

for x in '23456789':
    s = s.replace(x, '1')

split_plus = s.split('+')
plus = [[0, 0, 0] for _ in range(len(split_plus))]

for i in range(len(split_plus)):
    if check(split_plus[i]):
        plus[i][0] = len(split_plus[i])
    for j in range(1, len(split_plus[i])):
        if check(split_plus[i][:j]):
            plus[i][1] = j
        if check(split_plus[i][-j:]):
            plus[i][2] = j

c = 0
ans = -1
for i in range(len(plus)):
    if plus[i][0] > 0:
        c += (plus[i][0] + 1)
        ans = max(ans, c)
    else:
        if plus[i][1]:
            ans = max(ans, c + plus[i][1] + 1)
        if plus[i][2]:
            c = plus[i][2] + 1
        else:
            c = 0
print(ans - 1)