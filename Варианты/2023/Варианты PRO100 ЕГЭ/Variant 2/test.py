from itertools import product

count = 0

for i in product ('0123456', repeat=7):

  if i[0] != '0' and not ('12' in i and '35' in i):
    print(i)
    count += 1

print (count)