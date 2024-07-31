# 10-a, 11-b, 12-c...
for x in '0123456789abcdefg':
    a = int('68' + x + '68', 17)
    b = int(x + '6868', 17)
    if (a + b) % 16 == 0:
        print((a + b) // 16)

