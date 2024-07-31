with open('26_t.txt') as file:
    K, N = [int(x) for x in file.readline().split()]
    a = []
    for s in file:
        start, len_ = [int(x) for x in s.split()]
        a.append([start, start + len_])
a.sort(key=lambda x: x[1])
gran = -1
count = 0
history = []
for i in range(N):
    if a[i][0] >= gran:
        gran = a[i][1]
        count += 1
        history.append(a[i])

print(count * K)

a.sort()
for i in range(N):
    if a[i][0] >= history[-2][1]:
        print(a[i][0])
        break
