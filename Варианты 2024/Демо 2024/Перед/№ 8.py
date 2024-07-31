count = 0
for pos1 in '1234567':
    for pos2 in '01234567':
        for pos3 in '01234567':
            for pos4 in '01234567':
                for pos5 in '01234567':
                    s = pos1 + pos2 + pos3 + pos4 + pos5
                    if len(set(s)) == len(s):
                        if '1' not in s:
                            s = s.replace('1', 'n').replace('3', 'n').replace('5', 'n').replace('7', 'n').replace('9', 'n')
                            s = s.replace('0', 'c').replace('2', 'c').replace('4', 'c').replace('6', 'c').replace('8', 'c')
                            if ('nn' not in s) and ('cc' not in s):
                                count += 1
print(count)