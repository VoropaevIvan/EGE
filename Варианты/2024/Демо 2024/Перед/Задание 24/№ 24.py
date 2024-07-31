file = open('24_2024.txt')
s = file.readline().strip()
file.close()

s = 'T' + s + 'T'

pos_T = [i for i in range(len(s)) if s[i] == 'T']
otv = -1

for i in range(101, len(pos_T)):
    otv = max(otv, pos_T[i] - pos_T[i-101] - 1)

print(otv)

