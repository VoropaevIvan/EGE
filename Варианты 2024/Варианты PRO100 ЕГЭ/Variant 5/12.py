for n in range(4, 10_000):
    s = '5' + '2'*n
    while ('52' in s) or ('2222' in s) or ('1122' in s):
        if '52' in s:
            s = s.replace('52', '11', 1)
        if '2222' in s:
            s = s.replace('2222', '5', 1)
        if '1122' in s:
            s = s.replace('1122', '25', 1)
    sum_d = sum([int(x) for x in s])
    if sum_d % 10 == 7:
        print(n)
        break
