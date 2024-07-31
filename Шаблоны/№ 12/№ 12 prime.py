def prost(x):
    if x == 1:  # Единица - это не простое число!!!
        return 0
    for d in range(2, int(x**0.5) + 1):
        if x % d == 0:
            return 0
    return 1


s = '9' * 84
while ('33333' in s) or ('999' in s):
    if '33333' in s:
        s = s.replace('33333', '99', 1)
    else:
        s = s.replace('999', '3', 1)
print(s)
