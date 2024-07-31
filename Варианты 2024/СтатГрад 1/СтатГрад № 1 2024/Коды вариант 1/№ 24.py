file = open('24.txt')
s = 'A' + file.readline().strip() + 'A'

pred_AB = [['*', 0], ['*', 0], ['*', 0]]
ans = -1

for i in range(0, len(s)):
    if s[i] in 'AB':
        if pred_AB[1][0] + pred_AB[2][0] in ['AB', 'BA']:
            ans = max(ans, i - pred_AB[0][1] - 1)
        del pred_AB[0]
        pred_AB.append([s[i], i])
print(ans)
file.close()