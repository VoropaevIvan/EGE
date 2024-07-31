count = 0
for pos1 in '234567': # Без нуля!!!!!!
    for pos2 in '0234567':
        for pos3 in '0234567':
            for pos4 in '0234567':
                for pos5 in '0234567':
                    s = pos1 + pos2 + pos3 + pos4 + pos5
                    if len(set(s)) == len(s):
                        s = s.replace('1', 'n').replace('3', 'n').replace('5', 'n').replace('7', 'n')
                        s = s.replace('0', 'c').replace('2', 'c').replace('4', 'c').replace('6', 'c')
                        if ('nn' not in s) and ('cc' not in s):
                            count += 1
print(count)


