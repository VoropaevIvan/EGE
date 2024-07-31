import time
start_time = time.monotonic()

count = 0
for R in range(1_222_222_222, 1_555_555_666+1):
    r_2 = bin(R)[2:]
    pred = int(r_2[:-3], 2)
    if bin(pred % 5)[2:].zfill(3) == r_2[-3:]:
        pred = int(r_2[:-5], 2)
        if bin(pred % 3)[2:].zfill(2) == r_2[-5:-3]:
            count += 1

print(count)
print(f'Время работы программы = {time.monotonic() - start_time}')

# Время работы программы = 592.0160000000001