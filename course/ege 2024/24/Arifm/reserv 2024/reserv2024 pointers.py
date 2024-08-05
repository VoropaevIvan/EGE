with open('reserv153.txt') as file:
    s = file.readline().strip()
s = '0+10*1+0+0+0'
L = 0
R = -1
mul_zero_in = 0
for R in range(len(s)):
    if s[R] == '+':
        if mul_zero_in == 0:
            while L < R:
                L += 1
                if s[L] + s[L + 1] == '0*':
                    mul_zero_in = 1
                    break
    else:
        if s[max(L, R-1):R+1] in ['**', '*+', '+*', '++']:
            L = R + 1
    print(s[L:R+1])






