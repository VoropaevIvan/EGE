count = 0
for x in range(600_001, 10**10):
    flag_x = 0
    for d in range(2, x):
        if x % d == 0:
            if d % 10 == 9:
                flag_x = 1
                min_del_9 = d
                break
    if flag_x == 1:
        print(x, min_del_9)
        count += 1
        if count >= 5:
            break