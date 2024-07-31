def f(put):
    return sum(f(put + x) if (x not in put) else put[0] == x for x in d[put[-1]])


s = 'АВ БДА ВЕБ ГВБД ДЗ ЕЖ ЖКГ ЗГЖ КЗ'
d = {x[0]: x[1:] for x in s.split()}
print(f('Ж'))

