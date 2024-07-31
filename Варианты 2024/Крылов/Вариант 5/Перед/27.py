with open('27v05_T.txt') as file:
    N, M = [int(s) for s in file.readline().split()]
    km_bid = [0]*(28602671+1)
    for s in file:
        km, liters = [int(x) for x in s.split()]
        if liters % 15 == 0:
            km_bid[km] = liters // 15
        else:
            km_bid[km] = liters//15 + 1

ans_km = [0]*(28602671+1)
ans_km[0] = sum(km_bid[:M+1])
for i in range(1, 28602671+1):
    if i - M - 1 < 0:
        ans_km[i] = ans_km[i-1] + km_bid[i+M]
    if i - M - 1 >= 0 and i + M <= 28602671:
        ans_km[i] = ans_km[i-1] + km_bid[i+M] - km_bid[i-M-1]
    if i + M > 28602671:
        ans_km[i] = ans_km[i-1] - km_bid[i-M]

answer = -1
for i in range(1, 28602671+1):
    if km_bid[i] > 0:
        answer = max(answer, ans_km[i])
print(answer)


