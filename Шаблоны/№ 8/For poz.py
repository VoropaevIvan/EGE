k = 0
for p_0 in 'abzi':
    for p_1 in 'abzi':
        for p_2 in 'abzi':
            for p_3 in 'abzi':
                s = p_0 + p_1 + p_2 + p_3
                k += 1
                if s == 'izba':
                    print(k, s)
