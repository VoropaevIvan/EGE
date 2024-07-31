def f(put, end):
    return sum(1 if (x == end) else f(put + x, end) for x in d[put[-1]])


s = 'АБВГ БДВ ВДЖ ГВЕ ЕЖК ДИК ЖК ИК'
d = {x[0]: x[1:] for x in s.split()}
print(f('А', 'К'))

