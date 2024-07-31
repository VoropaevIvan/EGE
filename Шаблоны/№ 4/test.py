from itertools import *
def check_fano(kods):
    return all(not max(kods[i], kods[j]).startswith(min(kods[i], kods[j])) for i in range(len(kods)) for j in range(i + 1, len(kods)))

all_kods = [''.join(x) for i in range(1, 6+1) for x in product('01', repeat=i)]
otv = 10000
for a, v, t, s in combinations(all_kods, 4):
    if check_fano([a, v, t, s, '00', '01', '1000']):
        otv = min(otv, len(a)*3 + len(v)*2 + len(t) + 4 + 2 + 2)
print(otv)

#s = 'автолавка' # а3 в2 т1 о1 л1 к1 ц
# КАНТАТА
# k1 a3 t2 н1

