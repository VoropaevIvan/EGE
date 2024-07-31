file = open('24.txt')
s = file.readline().strip()
#s = 'AAeBBqqqqq'

otv = 0
for i in range(len(s)):
    count_A, count_B = 0, 0
    for j in range(i, len(s)):
        if s[j] == 'A':
            count_A += 1
        if s[j] == 'B':
            count_B += 1
        if count_A > 1 or count_B > 1:
            break
        if count_A == 1 and count_B == 1:
            s_t = s[i:j+1]
            if len(s_t) > otv:
                otv = len(s_t)
                print(s_t)


print(otv)
#file.close()