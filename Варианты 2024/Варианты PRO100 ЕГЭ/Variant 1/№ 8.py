alp = sorted('компьтер')
c = 0
for s1 in alp:
    for s2 in alp:
        for s3 in alp:
            for s4 in alp:
                for s5 in alp:
                    c += 1
                    s = s1 + s2 + s3 + s4 + s5
                    if c % 2 == 1 and s1 !='ь' and s.count('к') == 2:
                        print(c)

