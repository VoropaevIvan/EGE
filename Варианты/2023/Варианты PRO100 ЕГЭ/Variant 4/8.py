count = 0
for i1 in range(1, 16):
    for i2 in range(0, i1):
        for i3 in range(0, i2):
            count += 1

for i1 in range(1, 16):
    for i2 in range(0, i1):
        for i3 in range(0, i2):
            for i4 in range(0, i3):
                for i5 in range(0, i4):
                    count += 1
print(count)