def solve_2(s):
    digits = '0123456789'

    def zero(s):
        return '*0*' in '*' + s + '*'

    def maxZeroLength(s):
        s = s.split('+')
        n = len(s)
        partLen = [(len(p) + 1 if zero(p) else 0) for p in s]
        dp = [0] * n
        dp[0] = partLen[0]
        for i in range(1, n):
            dp[i] = dp[i - 1] + partLen[i] if partLen[i] > 0 else 0
        return max(dp) - 1

    def check(expr):
        global maxLen
        curLen = maxZeroLength(expr)
        if curLen > maxLen:
            print('>', expr)
            maxLen = curLen

    maxLen = 0
    state = 0  # start number
    expr = ''
    for i, c in enumerate(s):
        if state == 0:
            if c in digits:
                expr += c
                check(expr)
                state = 1  # continue number or operation
            else:
                expr = ''
        elif state == 1:
            if c in digits:
                expr += c
                check(expr)
            else:
                expr += c
                state = 0

    return (maxLen)
