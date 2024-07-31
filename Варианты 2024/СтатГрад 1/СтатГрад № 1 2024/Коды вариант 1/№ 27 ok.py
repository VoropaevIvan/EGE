with open('27-T.txt') as file:
    k = int(file.readline())
    a = [int(file.readline()) for s in range(int(file.readline()))]

ans = -10000000
max_3k = -100000000
m_2, m_1 = sorted(a[:3*k])[-2:]

for i in range(3*k, len(a)):
    max_3k = max(max_3k, a[i - 3*k])
    if m_1 != max_3k:
        ans = max(ans, m_1 + max_3k + a[i])
    else:
        ans = max(ans, m_2 + max_3k + a[i])

    _, m_2, m_1 = sorted([m_1, m_2, a[i]])

print(ans)
