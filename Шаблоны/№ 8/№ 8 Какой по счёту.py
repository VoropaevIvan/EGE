from itertools import *

for i, x in enumerate(product('аклмня', repeat=5),start=1):
    print(i, x)
    if x[0] + x[1] == 'км':
        print(i)
        break

