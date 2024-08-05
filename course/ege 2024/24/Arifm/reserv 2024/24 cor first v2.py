with open('reserv142.txt') as file:
    s = file.readline().strip()

#s = '++++01++++1'
# s = '11110+001'
s = '++' + s + '++'
ok_exprs = []
cur_expr = ''
for i in range(1, len(s)):
    if cur_expr[-1:] + s[i] in ['++', '**', '*+', '+*']:
        ok_exprs.append(cur_expr[:-1])
        cur_expr = ''
    elif cur_expr[-2:] + s[i] in ['+01', '*01', '+00', '*00']:
        ok_exprs.append(cur_expr)
        cur_expr = s[i]
    elif cur_expr + s[i] in ['+', '*']:
        cur_expr = ''
    elif cur_expr == '0' and s[i] in '0123456789':
        cur_expr = s[i]
    else:
        cur_expr += s[i]

#print(ok_exprs)
#exit()
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
        # print(cur_ans[1:])
        ans = max(ans, len(cur_ans[1:]))

print(ans)
