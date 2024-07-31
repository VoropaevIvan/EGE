ans = 0
nomer = 1
for b1 in 'АВИОРТФ':
    for b2 in 'АВИОРТФ':
        for b3 in 'АВИОРТФ':
            for b4 in 'АВИОРТФ':
                for b5 in 'АВИОРТФ':
                    for b6 in 'АВИОРТФ':
                        s = b1 + b2 + b3 + b4 + b5 + b6
                        if s[0] != 'О':
                            if nomer % 2 == 0:
                                if s.count('Р') == 2:
                                    ans += 1
                        nomer += 1
print(ans)