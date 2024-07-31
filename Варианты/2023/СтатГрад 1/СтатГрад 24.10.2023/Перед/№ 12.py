def prime(x):
    if x == 1:
        return False
    for d in range(2, int(x**0.5)+1):
        if x % d == 0:
            return False
    return True


ans = []
for count_1 in range(0, 200):
    for count_2 in range(0, 200):
        if count_1 + count_2 <= 40:
            continue

        s = '0' + count_1*'1' + count_2*'2'
        sum_start = sum(map(int, s))

        while ('01' in s) or ('02' in s):
            s = s.replace('02', '1110', 1)
            s = s.replace('01', '220', 1)

        sum_end = sum(map(int, s))
        if prime(sum_end):
            if sum_start == 42:
                print(sum_start, sum_end, count_1, count_2)
            ans.append(sum_start)

print(min(ans))

