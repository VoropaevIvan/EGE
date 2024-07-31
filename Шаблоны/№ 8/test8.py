k = 0
count = 0
for pos1 in 'ЬРПЛЕА':
    for pos2 in 'ЬРПЛЕА':
        for pos3 in 'ЬРПЛЕА':
            for pos4 in 'ЬРПЛЕА':
                for pos5 in 'ЬРПЛЕА':
                    s = pos1 + pos2 + pos3 + pos4 + pos5
                    k += 1
                    if k <= 387:
                        if s[-1] == 'Ь':
                            count += 1
print(count)
