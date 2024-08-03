with open('reserv153.txt') as file:
    s = file.readline().strip()
ans = -1
for i in range(len(s)):
    for j in range(10):
        t = s[i:i+j+1]
        a = ['++', '+-', '--', '-+']
        if all(x not in t for x in a):
            try:
                if eval(t) == 0:
                    #print(t)
                    ans = max(ans, len(t))
            except:
                ...
print('ok')