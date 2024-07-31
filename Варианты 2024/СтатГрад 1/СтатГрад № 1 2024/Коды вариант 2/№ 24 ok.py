file = open('24.txt')
s = 'X' + file.readline().strip() + 'Y'

pred = [['*', 0], ['*', 0],['*', 0]]
ans = -1

for i in range(0, len(s)):
    if s[i] in 'XY':
        if pred[1][0] + pred[2][0] in ['XY', 'YX']:
            ans = max(ans, i - pred[0][1] - 1)
        del pred[0]
        pred.append([s[i], i])
print(ans)
file.close()