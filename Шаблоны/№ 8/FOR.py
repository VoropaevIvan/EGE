otv = 0
for pos1 in 'skola':
    for pos2 in 'skola':
        for pos3 in 'skola':
            s = pos1 + pos2 + pos3
            if s.count('k') == 1:
                otv += 1
print(otv)
