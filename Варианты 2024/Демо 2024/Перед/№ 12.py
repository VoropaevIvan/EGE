for n in range(4, 10_000):
    s = '5' + '2'*n

    while ('52' in s) or ('2222' in s) or ('222' in s):
        if '52' in s:
            s = s.replace('52', '11', 1)
        if '2222' in s:
            s = s.replace('2222', '5', 1)
        if '1122' in s:
            s = s.replace('1122', '25', 1)

    sum_ = s.count('1') + 2*s.count('2') + 5*s.count('5')
    if sum_ == 64:
        print(n)





sum_ = sum(map(int, s))
sum_ = sum(int(x) for x in s)