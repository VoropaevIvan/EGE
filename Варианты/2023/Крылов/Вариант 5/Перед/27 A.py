with open('27v05_A.txt') as file:
    N, M = [int(s) for s in file.readline().split()]
    km_bid = [0]*(5000+1)
    for s in file:
        km, liters = [int(x) for x in s.split()]
        if liters % 15 == 0:
            km_bid[km] = liters // 15
        else:
            km_bid[km] = liters//15 + 1

answer = -1
for i in range(0, 5000+1):
    if km_bid[i] == 0:
        continue
    sum_ = 0
    for j in range(i-M, i+M+1):
        if j < 0 or j > 5000:
            continue
        sum_ += km_bid[j]
    answer = max(answer, sum_)

print(answer)


