def solve_3(s):
    def check(s):
        for x in '23456789':
            s = s.replace(x, '1')
        des = 1
        for split_plus in s.split('+'):
            split_mult = split_plus.split('*')
            des_t = ('0' in split_mult) and ('' not in split_mult) and all(
                x[:2] not in ['00', '01'] for x in split_mult)
            if des_t == 0:
                des = 0
        if des == 1 and eval(s) != 0:
            print('ERROR!!!!!!!!!!!!!!!!')
        return des

    ans = -1
    for i in range(len(s)):
        for j in range(i, len(s)):
            if check(s[i:j + 1]):
                ans = max(ans, j - i + 1)
    if ans == 1:
        return -1
    return ans