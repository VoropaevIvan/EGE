file = open('27-T.txt')
k = int(file.readline())
a = [int(file.readline()) for s in range(int(file.readline()))]

ans = -1
max_pref = [-100000000]*(len(a)+1)
m_1, m_2 = -10000000, -1000000

for i in range(len(a)):
    if i - 2*k >= 0:
        left = max_pref[i-2*k]
        if m_1 != left:
            ans = max(ans, m_1 + left + a[i])
        else:
            ans = max(ans, m_2 + left + a[i])
    _, m_2, m_1 = sorted([m_1, m_2, a[i]])
    max_pref[i] = max(max_pref[i-1], a[i])

print(ans)

file.close()