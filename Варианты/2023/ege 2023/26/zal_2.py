with open('26_zal.txt') as file:
    n = int(file.readline())
    a = []
    for s in file:
        start, end = [int(x) for x in s.split()]
        a.append([start, end])


a.sort(key=lambda x: x[1])

events_which_we_take = [[-1, -1]]
count = 0
for i in range(n):
    if events_which_we_take[-1][1] <= a[i][0]:
        count += 1
        events_which_we_take.append([a[i][0], a[i][1]])


# Second question
end_second = events_which_we_take[-2][1]
ans_2 = -1
for event in a:
    if end_second <= event[0]:
        ans_2 = max(ans_2, event[1])

print(count, ans_2)
