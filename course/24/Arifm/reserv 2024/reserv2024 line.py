with open('reserv153.txt') as file:
    s = file.readline().strip()
s = '0+10*1+0+0+0'
#s = '**' + s + '**'
start = 0
mul_zero_in = 0
ans = -1
extra = [-1, 0]
cur_extra = -1
for i in range(0, len(s)):
    if s[i] in '123456789':
        if start <= i-2 and s[i - 2] + s[i - 1] + s[i] in ['+01', '*01']:
            start = i
            mul_zero_in = 0
            extra = [-1, 0]
            cur_extra = -1
        if mul_zero_in:
            print(s[start:i + 1])
            ans = max(ans, i - start + 1)
            if extra[0] != -1:
                print(s[extra[0]:i + 1])
                ans = max(ans, i - extra[0] + 1)
        if cur_extra != -1:
            print(s[cur_extra:i + 1])
            ans = max(ans, i - cur_extra + 1)
    if s[i] == '0':
        if start <= i-2 and s[i-2] + s[i-1] + s[i] in ['+00', '*00']:
            start = i
            extra = [-1, 0]
            cur_extra = -1
        if start <= i-1 and s[i-1] + s[i] == '*0':
            mul_zero_in = 1
        if mul_zero_in:
            print(s[start:i+1])
            ans = max(ans, i - start + 1)
            if extra[0] != -1:
                print(s[extra[0]:i + 1])
                ans = max(ans, i - extra[0] + 1)
        if start <= i-1 and s[i-1] == '+':
            print('!!!!!!!!!!!!!!!!!')
            mul_zero_in = 1
            print(s[start:i + 1])
            ans = max(ans, i - start + 1)
        else:
            print('!!!!!', start, i-1)
        if extra[0] != -1 and s[i-1] == '+':
            print(s[extra[0]:i + 1])
            ans = max(ans, i - extra[0] + 1)
    if s[i] == '*':
        if (start == i-1) and s[i-1] == '0':
            mul_zero_in = 1
        if (start <= i-1) and s[i-1] + s[i] in ['**', '+*']:
            mul_zero_in = 0
            start = i + 1
            extra = [-1, 0]
            cur_extra = -1
        if start == i:
            start = i + 1
            extra = [-1, 0]
            cur_extra = -1
        if extra[0] == -1 and start <= i - 1 and s[i-1] + s[i] == '0*':
            extra = [i-1, 1]
        if cur_extra == -1 and start <= i - 1 and s[i-1] + s[i] == '0*':
            cur_extra = i-1
    if s[i] == '+':
        if (start <= i-1) and s[i-1] + s[i] in ['*+', '++']:
            mul_zero_in = 0
            start = i + 1
        if mul_zero_in == 0:
            extra[1] = extra[1] - 1
            if extra[1] == -1:
                if cur_extra != -1:
                    extra = [cur_extra, 1]
                else:
                    extra = [-1, 0]
            start = i+1
        else:
            mul_zero_in = 0
        if start == i:
            start = i + 1
        cur_extra = -1
    print(extra, mul_zero_in, start)

print(ans)


