with open('test.txt') as file:
    N = int(file.readline())
    a = [int(x) for x in file]
min_sum = 10**10
len_ = -1
for i in range(len(a)):
    cur_sum = a[i]
    for j in range(i+1, len(a)):
        cur_sum += a[j]
        if cur_sum % 2 == 1:
            if cur_sum == min_sum:
                len_ = max(len_, j-i+1)
            elif cur_sum < min_sum:
                min_sum = cur_sum
                len_ = j - i + 1

print(len_)