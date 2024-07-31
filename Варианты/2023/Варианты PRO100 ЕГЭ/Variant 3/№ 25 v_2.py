for x in range(133, 10**10+1, 133):
    x_s = str(x)
    if 7 <= len(x_s):
        if x_s[0] == '1':
            if x_s[1] in '02468':
                if x_s[2:6] == '2157':
                    if x_s[-1] == '4':
                        if all(t in '13579' for t in x_s[6:-1]):
                            print(x, x // 133)