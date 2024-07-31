count = 0
for b_1 in 'АГЛОЬ':
    for b_2 in 'АГЛОЬ':
        for b_3 in 'АГЛОЬ':
            for b_4 in 'АГЛОЬ':
                for b_5 in 'АГЛОЬ':
                    s = b_1 + b_2 + b_3 + b_4 + b_5
                    count += 1
                    if s == 'ОЛЬГА':
                        print(count)
