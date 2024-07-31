f = open('27_A.txt')
n = int(f.readline())
a = [int(x) for x in f]

otv = -1000000
max_pref = a[0]

for i in range(1, n):
    otv = max(otv, max_pref + a[i] + i)
    max_pref = max(max_pref, a[i] - i)

print(otv)
f.close()

# 10733 6231338
