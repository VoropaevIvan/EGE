from itertools import *
def check_fano(kods):
    return all(not max(kods[i], kods[j]).startswith(min(kods[i], kods[j])) for i in range(len(kods)) for j in range(i + 1, len(kods)))

all_kods = [''.join(x) for i in range(1, 6+1) for x in product('01', repeat=i)]

for z, q in combinations(all_kods, 2):
    if check_fano([z, q, *'11 0010 100 0011 01 000'.split()]):
        print(z, q)



# КАНТАТА
# k1 a3 t2 н1

