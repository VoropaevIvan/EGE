otv = 0
for pos1 in '246':  # Без нуля!!!!!!!!!!!!!!!
    for pos2 in '01234567':
        for pos3 in '01234567':
            for pos4 in '567':
                s = pos1 + pos2 + pos3 + pos4
                if s.count('6') > 2:
                    otv += 1
print(otv)
