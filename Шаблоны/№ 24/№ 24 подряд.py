f = open('24.txt')
s = f.readline()

s = s.replace('AB', '+').replace('CB', '+')

for i in range(1, 10000000):
    t = '+'*i
    if t in s:
        print(i)
    else:
        break
f.close()
