with open('day_1_centre_test.txt') as file:
    N, count_ryd, count_nomer = [int(x) for x in file.readline().split()]
    a = []
    for s in file:
        ryd, mesto = [int(x) for x in s.split()]
        a.append([ryd, mesto])

d = [10**10]*(count_nomer+1)
for ryd, mesto in a:
    d[mesto] = min(d[mesto], ryd-1)
ans_ryd = -1
ans_mesto = -1
for i in range(2, count_nomer+1):
    cur_ryd = min(d[i-1], d[i])
    if cur_ryd > ans_ryd:
        ans_ryd = cur_ryd
        ans_mesto = i
    elif cur_ryd == ans_ryd:
        ans_mesto = i
print(ans_ryd, ans_mesto)


