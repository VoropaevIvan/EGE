with open('files/17.txt') as file:
    a = [int(s) for s in file]
min_ = min(a) % 3
max_ = max(a) % 7
ans = []
for i in range(1, len(a)):
    x = a[i - 1]
    y = a[i]
    if (x % 3 == min_) or (y % 3 == min_):
        if (x % 7 == max_) or (y % 7 == max_):
            ans.append(x + y)
print(len(ans), max(ans))
