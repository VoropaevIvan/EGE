count = 0
for pos1 in 'АВРО':  # Выписываем только УНИКАЛЬНЫЕ буквы, без повторов.
    for pos2 in 'АВРО':
        for pos3 in 'АВРО':
            for pos4 in 'АВРО':
                for pos5 in 'АВРО':
                    for pos6 in 'АВРО':
                        s = pos1 + pos2 + pos3 + pos4 + pos5 + pos6
                        if s.count('А') == 2 and s.count('В') == 1 and s.count('Р') == 2 and s.count('О') == 1:
                            if ('АА' not in s) and ('РР' not in s):
                                count += 1
print(count)
