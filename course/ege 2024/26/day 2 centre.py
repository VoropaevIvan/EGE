with open('26day2centre.txt') as file:
    N, K = [int(x) for x in file.readline().split()]
    a = []
    balls = set()
    for s in file:
        id_, score1, score2, score3, sobes = [int(x) for x in s.split()]
        a.append([score1+score2+score3, sobes, id_])
        balls.add(score1+score2+score3)
a.sort(key=lambda x:[x[0], x[1], -x[2]], reverse=True)

# ans 1
polu_score = a[K-1][0]
for i in range(K-1, 0, -1):
    if a[i][0] != polu_score:
        print(a[i][2])
        break
# ans 2
count_pol = 0
for sum_, sobes, id_ in a:
    if sum_ == polu_score:
        count_pol += 1
print(count_pol)
