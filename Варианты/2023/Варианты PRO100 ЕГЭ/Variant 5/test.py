c = 0
a = [0]*10000
for i in range(len(a)):
    for j in range(len(a)):
        for k in range(len(a)):
            c += i

print(c)
