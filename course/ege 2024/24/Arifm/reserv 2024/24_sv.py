file = open("24.txt")
s = file.readline()
# s = '12330'
# print('*000' in s) # проверка - есть ли в строке конструкции "знак+много нулей" - нет таких конструкций

# создаём список правильных строк без двух знаков подряд, без ведущих нулей
a = []
t = '0+'
for i in range(2, len(s)):
    if s[i] in '+*':
        if s[i - 1] in '+*':
            a.append(t[:-1:])
            t = ''
        else:
            t += s[i]
    elif s[i] in '123456789':
        if s[i - 1] == '0':
            if s[i - 2] in '+*':
                a.append(t)
                t = s[i]
            else:
                t += s[i]
        else:
            t += s[i]
    else:
        t += s[i]
a.append(t)
# print(a)


max_ = 0
for t in a:
    l_sl = t.split('+')
    k = 0
    pl = 0
    for sl in l_sl:
        if '*0*' in sl or '0*' == sl[:2] or '*0' == sl[-2:] or sl == '0':
            k += len(sl)
            pl += 1
        else:
            pl = 0
            k = 0
            if '0*' in sl:
                k = len(sl[sl.find('0*'):])
                pl = 1
            elif sl != '' and sl[-1] == '0':  # 130
                k = 1
                pl = 1
        max_ = max(max_, k + pl - 1)

print(max_)
