import time
start_time = time.monotonic()

st = set()
count = 0
for N in range(1, 1_444_444_416):
    n_2 = bin(N)[2:]

    ost = bin(N % 3)[2:].zfill(2)
    n_2 = n_2 + ost
    r = int(n_2, 2)

    ost = bin(r % 5)[2:].zfill(3)
    n_2 = n_2 + ost
    r = int(n_2, 2)

    if 1_111_111_110 <= r <= 1_444_444_416:
        st.add(r)

print(len(st))
print(f'Время работы программы = {time.monotonic() - start_time}')


# 1916.405999999959