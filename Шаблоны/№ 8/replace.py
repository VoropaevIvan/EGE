otv = 0
for pos1 in '1234567':  # Без нуля!!!!!!!!!!!!!!!
    for pos2 in '01234567':
        for pos3 in '01234567':
            for pos4 in '01234567':
                for pos5 in '01234567':
                    s = pos1 + pos2 + pos3 + pos4 + pos5
                    s = s.replace('1', 'n').replace('3', 'n').replace('5', 'n').replace('7', 'n')
                    if s.count('6') == 1:
                        if ('n6' not in s) and ('6n' not in s):
                            otv += 1
print(otv)
