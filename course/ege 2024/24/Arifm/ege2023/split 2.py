with open('ege2023.txt') as file:
    s = file.readline().strip()

s = s.replace('++', ' ')

ans = -1
for x in s.split():
    x = x.strip('+')
    if '+' in x:
        print(x)
        ans = max(ans, len(x))
print(ans)