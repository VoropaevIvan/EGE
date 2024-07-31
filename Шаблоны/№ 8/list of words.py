k = 0
for pos1 in 'abrti':
    for pos2 in 'abrti':
        for pos3 in 'abrti':
            for pos4 in 'abrti':
                for pos5 in 'abrti':
                    s = pos1 + pos2 + pos3 + pos4 + pos5
                    k += 1
                    if ('i' not in s) and ('aa' not in s):
                        print(k)