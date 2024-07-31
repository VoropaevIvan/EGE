with open('26.txt') as file:
    N, K = [int(x) for x in file.readline().split()]
    lenta = [-1] * (N + 1)
    L = 1
    R = N
    count_o = 0
    for i in range(1, N+1):
        time_o, time_s = [int(x) for x in file.readline().split()]
        if time_s < time_o:
            lenta[L] = i
            L += 1
        else:
            lenta[R] = i
            R -= 1
            count_o += 1
print(count_o, lenta[K])

