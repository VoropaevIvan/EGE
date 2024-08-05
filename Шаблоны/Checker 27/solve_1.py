def solve_1(s):
    s = ' ' + s + ' '
    for x in '23456789':
        s = s.replace(x, '1')
    for x in ['++', '*+', '+*', '**']:
        s = s.replace(x, ' ')
    for x in ['* ', '+ ', ' *', ' +']:
        s = s.replace(x, ' ')

    s = s.replace('+01', '+0 1')
    s = s.replace('*01', '*0 1')
    s = s.replace('+00', '+0 0')
    s = s.replace('*00', '*0 0')
    while ' 00' in s:
        s = s.replace(' 00', ' 0 0')
    s = s.replace(' 01', ' 0 1')

    ans = -1
    for cur_expr in s.split():
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
                # print(cur_ans[1:])
                ans = max(ans, len(cur_ans[1:]))

    if ans == 1:
        return -1
    return ans