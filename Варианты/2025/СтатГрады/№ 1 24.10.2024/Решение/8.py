count = 0
for x1 in '123456789ABCDE':
    for x2 in '0123456789ABCDE':
        for x3 in '0123456789ABCDE':
            for x4 in '0123456789ABCDE':
                for x5 in '0123456789ABCDE':
                    for x6 in '0123456789ABCDE':
                        for x7 in '0123456789ABCDE':
                            for x8 in '0123456789ABCDE':
                                s = x1+x2+x3+x4+x5+x6+x7+x8
                                if s.count('0') == 2:
                                    if s.count('A')+s.count('B')+s.count('C')+s.count('D')+s.count('E') <= 4:
                                        count += 1
                                print(x1)
print(count)
