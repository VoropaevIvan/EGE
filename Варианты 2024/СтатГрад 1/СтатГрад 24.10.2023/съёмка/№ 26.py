with open('26.txt') as file:
    n = int(file.readline())
    a = []
    for s in file:
        start, end = [int(x) for x in s.split()]
        a.append([start, end])

a.sort(key=lambda x: x[1])

events_which_we_make = [[-10000, -10000]]

for i in range(n):
    start, end = a[i]
    if events_which_we_make[-1][1] + 15 <= start:
        events_which_we_make.append([start, end])

gran = events_which_we_make[-2][1]
max_pereriv= -1000
for i in range(n):
    if gran + 15 <= a[i][0]:
        max_pereriv = max(max_pereriv, a[i][0] - gran)


print(len(events_which_we_make) - 1, max_pereriv)
