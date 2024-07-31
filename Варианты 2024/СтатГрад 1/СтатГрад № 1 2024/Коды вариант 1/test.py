import time
start_time = time.monotonic()

for i in range(1, 20):
    n_2 = bin(i)[2:]
    print(i % 3, n_2)

exit()
st = set()
count = 0
for N in range(1, 1_444_444_416):
    n_2 = bin(N)[2:]
    print(N, n_2, end=' ')

    ost = bin(N % 3)[2:].zfill(2)
    n_2 = n_2 + ost
    r = int(n_2, 2)
    print(n_2, end=' ')

    ost = bin(r % 5)[2:].zfill(3)
    n_2 = n_2 + ost
    r = int(n_2, 2)
    print(n_2, end=' ')

    print(r)

print(len(st))
print(f'Время работы программы = {time.monotonic() - start_time}')


# 1916.405999999959