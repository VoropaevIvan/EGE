# 10-a, 11-b, 12-c...
for x in '0123456789abcdefghi':
    a = int('78' + x + '79643', 19)
    b = int('25' + x + '43', 19)
    c = int('63' + x + '5', 19)
    if (a + b + c) % 18 == 0:
        print((a + b + c) // 18)

