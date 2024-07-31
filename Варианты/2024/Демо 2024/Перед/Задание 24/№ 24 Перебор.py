file = open('24_2024.txt')
s = file.readline().strip()

otv = -1
for i in range(len(s)):
    count_T = 0
    for j in range(i, len(s)):
        s_t = s[i:j+1]
        if s_t.count('T') == 100:
            otv_t = j - i + 1
            if otv_t > otv:
                print(otv_t)
                otv = otv_t
        if s_t.count('T') > 100:
            break

file.close()