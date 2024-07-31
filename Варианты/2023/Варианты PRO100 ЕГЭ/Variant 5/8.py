count = 0
for b1 in 'ПРОСТО':
    for b2 in 'ПРОСТО':
        for b3 in 'ПРОСТО':
            for b4 in 'ПРОСТО':
                for b5 in 'ПРОСТО':
                    for b6 in 'ПРОСТО':
                        s = b1 + b2 + b3 + b4 + b5 + b6
                        if sorted(s) == sorted('ПРОСТО'):
                            if 'ОО' not in s:
                                count += 1
print(count)

