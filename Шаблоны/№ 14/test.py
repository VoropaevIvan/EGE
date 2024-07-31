# 10-a, 11-b, 12-c
for x in '0123456789':
    base_1 = int('68' + x + '68')
    base_2 = int('1234' + x)
    a = 1*base_1**1 + 2*base_1**0
    b = 2*base_2**1 + 2*base_2**0
    if (a + b) % 2 == 0:
        print((a + b) // 2)
