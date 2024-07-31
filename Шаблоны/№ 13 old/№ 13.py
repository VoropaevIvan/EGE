def f(t, put):
    global otv
    for x in d[t]:
        if x in put:
            if put[0] == x:
                print(put + x)
                otv += 1
        else:
            f(x, put + x)


s = 'АВ БДА ВЕБ ГВБД ДЗ ЕЖ ЖКГ ЗГЖ КЗ'
d = {x[0]: x[1:] for x in s.split()}

otv = 0
start = 'Ж'

f(start, start)
print(otv)
