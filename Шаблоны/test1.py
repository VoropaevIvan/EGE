otv = 0
for pos1 in '123456789':  # Без нуля!!!!!!!!!!!!!!!
    for pos2 in '0123456789':
        for pos3 in '0123456789':
            for pos4 in '0123456789':
                for pos5 in '0123456789':
                    for pos6 in '0123456789':
                        s = pos1 + pos2 + pos3 + pos4 + pos5 + pos6
                        if len(set(s)) == 6:
                            for i in '02468':
                                s = s.replace(i, 'c')
                            for i in '13579':
                                s = s.replace(i, 'n')
                            if 'cc' not in s and 'nn' not in s:
                                otv += 1
print(otv)
