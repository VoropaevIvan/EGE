with open('test.txt') as file:
    N = int(file.readline())
    a = [int(x) for x in file]

max_len = -1
for i in range(len(a)):
    cur_sum = a[i]
    for j in range(i+1, len(a)):
        cur_sum += a[j]
        if cur_sum < 0 and cur_sum % 2 == 1:
            max_len = max(max_len, j-i+1)
print(max_len)
