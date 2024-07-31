f = open('24.txt')
s = f.readline()
s = s.replace('A', '-').replace('B', '-').replace('C', '-')
s = s.replace('--', '- -').replace('--', '- -')
a = s.split()
otv = max(a, key=len)
print(len(otv))

