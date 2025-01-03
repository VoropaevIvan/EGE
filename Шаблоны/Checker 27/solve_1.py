def solve_1(s):
    for x in '23456789':
        s = s.replace(x, '1')

    ok_exprs = []
    s = s.lstrip('+*')
    if s == '':
        return -1
    cur = s[0]
    s = s + '**'
    for i in range(1, len(s)):
        cur += s[i]
        if cur[-2:] in ['++', '**', '+*', '*+']:
            ok_exprs.append(cur[:-2])
            cur = ''
        elif cur[-3:] in ['+00', '+01', '*00', '*01']:
            ok_exprs.append(cur[:-1])
            cur = s[i]
        elif cur[:2] in ['00', '01']:
            cur = s[i]
        elif cur in ['*', '+']:
            cur = ''

    ans = -1
    for cur_expr in ok_exprs:
        cur_ans = ''
        for mul_expr in cur_expr.split('+'):
            if (mul_expr[:2] == '0*') or (mul_expr[-2:] == '*0') or ('*0*' in mul_expr) or (mul_expr == '0'):
                cur_ans += ('+' + mul_expr)
            else:
                if '0*' in mul_expr:
                    pos = mul_expr.find('0*')
                    cur_ans = '+' + mul_expr[pos:]
                elif mul_expr[-1] == '0':
                    cur_ans = '+0'
                else:
                    cur_ans = ''
            if ('+' in cur_ans[1:]) or ('*' in cur_ans[1:]):
                #print(cur_ans[1:])
                ans = max(ans, len(cur_ans[1:]))

    return (ans)