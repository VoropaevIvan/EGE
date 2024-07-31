count = 0
for b_1 in 'АВЕСТ':
    for b_2 in 'АВЕСТ':
        for b_3 in 'АВЕСТ':
            for b_4 in 'АВЕСТ':
                for b_5 in 'АВЕСТ':
                    s = b_1 + b_2 + b_3 + b_4 + b_5
                    count += 1
                    if s == 'СВЕТА':
                        print(count)


