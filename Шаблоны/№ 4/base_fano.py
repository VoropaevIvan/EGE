def load_kods(x):
    if len(x) == 8:
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

ready_kods = '00 1000 010 011 1011 1001 1010 1101 111'
ready_kods = [x for x in ready_kods.split()]

otv = set()
for d in kods:
    if check_fano(ready_kods + [d]):
        otv.add(d)
otv = sorted(otv, key=len)
print(otv)

