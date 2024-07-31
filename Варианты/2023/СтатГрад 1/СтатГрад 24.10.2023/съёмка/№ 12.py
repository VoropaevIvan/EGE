def prime(x):
    if x == 1:
        return False
    for d in range(2, int(x**0.5) + 1):
        if x % d == 0:
            return False
    return True

answer = []
for count_1 in range(0, 200):
    for count_2 in range(0, 200):
        s = '0' + '1'*count_1 + '2'*count_2
        sum_start = sum([int(x) for x in s])
        if len(s) <= 40:
            continue
        while ('01' in s) or ('02' in s):
            s = s.replace('02', '1110', 1)
            s = s.replace('01', '220', 1)

        sum_end = sum([int(x) for x in s])
        if prime(sum_end):
            answer.append(sum_start)


print(min(answer))

