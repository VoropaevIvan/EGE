def solve_2(a):
    s = a

    l = 0
    r = -1
    count_A = 0
    count_B = 0
    ans = -1
    while True:
        if count_A <= 2 and count_B <= 2:
            ans = max(ans, r - l + 1)
            r += 1
            if len(s) == r:
                break
            if s[r] == 'A':
                count_A += 1
            if s[r] == 'B':
                count_B += 1
        else:
            l += 1
            if s[l - 1] == 'A':
                count_A -= 1
            if s[l - 1] == 'B':
                count_B -= 1

    return ans