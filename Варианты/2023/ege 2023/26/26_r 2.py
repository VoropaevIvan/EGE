with open('26_rt.txt') as file:
    n = int(file.readline())
    time_razn = dict()
    for s in file:
        start, end = [int(x) for x in s.split()]
        if start in time_razn:
            time_razn[start] += 1
        else:
            time_razn[start] = 1
        if end in time_razn:
            time_razn[end] -= 1
        else:
            time_razn[end] = -1

cur_ball = 0
max_bal = -1
count_piks = 0
for x in sorted(time_razn):
    if time_razn[x] == 0:
        continue
    cur_ball += time_razn[x]
    if cur_ball == max_bal:
        count_piks += 1
    if cur_ball > max_bal:
        max_bal = cur_ball
        count_piks = 1

print(count_piks, max_bal)