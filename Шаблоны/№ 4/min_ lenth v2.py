from itertools import *
def check_fano(kods):
    return all(not max(kods[i], kods[j]).startswith(min(kods[i], kods[j])) for i in range(len(kods)) for j in range(i + 1, len(kods)))

all_kods = [''.join(x) for i in range(1, 6+1) for x in product('01', repeat=i)]
otv = 10000
for a, t, z in combinations(all_kods, 3):
    if check_fano([a, t, z, '1', '001']):
        otv = min(otv, 1 + 3 + len(a)*3 + len(t)*2)
print(otv)


# КАНТАТА
# k1 a3 t2 н1

