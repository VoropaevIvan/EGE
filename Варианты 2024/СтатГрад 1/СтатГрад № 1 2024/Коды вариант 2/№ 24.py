file = open('24.txt')
s = file.readline().strip()
#s = 'AAeBBqqqqq'

otv = 0
for i in range(len(s)):
    count_X, count_Y = 0, 0
    for j in range(i, len(s)):
        if s[j] == 'X':
            count_X += 1
        if s[j] == 'Y':
            count_Y += 1
        if count_X > 1 or count_Y > 1:
            break
        if count_X == 1 and count_Y == 1:
            s_t = s[i:j+1]
            otv = max(otv, len(s_t))


print(otv)
file.close()