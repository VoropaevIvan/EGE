file = open('26.txt')
n = int(file.readline())

a = [[int(x) for x in s.split()] for s in file]
a.sort()
most_late_start = a[-1][0]
a.sort(key=lambda x: x[1])

events_which_we_take = [[-1, -1]]
count = 0
for i in range(n):
    if events_which_we_take[-1][0] + 15 <= a[i][0]:
        count += 1
        events_which_we_take.append([a[i][0] + 15, a[i][1]])


# Second question
end_second = events_which_we_take[-2][1]
ans_2 = -1
for event in a:
    if end_second + 15 <= event[0]:
        ans_2 = max(ans_2, event[0] - end_second)

print(count, ans_2)










file.close()