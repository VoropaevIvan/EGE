def load_kods(x):
    if len(x) == 7:
        return
    if x:
        kods.append(x)
    load_kods(x + '0')
    load_kods(x + '1')


def check_fano(all_kods):
    for i in range(len(all_kods)):
        for j in range(i + 1, len(all_kods)):
            if all_kods[i].startswith(all_kods[j]) or all_kods[j].startswith(all_kods[i]):
                return 0
    return 1


kods = []
load_kods('')
print(len(kods))

ready_kods = '0 11'
ready_kods = [x for x in ready_kods.split()]
print(len(kods))
kods = [x for x in kods if check_fano(ready_kods + [x])]
print(len(kods))

otv = set()
otv.add(100000)
for a in kods:
    for i in kods:
        for k in kods:
            for t in kods:
                if len(a) * 2 + len(k) * 2 + len(t) * 1 + len(i) + 1 > min(otv):
                    continue
                if check_fano(ready_kods + [a, i, k, t]):
                    otv.add(len(a) * 2 + len(k) * 2 + len(t) * 1 + len(i) + 1)
otv = sorted(otv)
print(otv)
