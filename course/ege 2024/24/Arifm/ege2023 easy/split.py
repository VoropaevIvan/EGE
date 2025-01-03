import string

with open('24.txt') as file:
    s = file.readline().strip()

for x in string.ascii_uppercase[6:]:
    s = s.replace(x, ' ')

ans = -1
for x in s.split():
    print(x)
    ans = max(ans, len(x))
print(ans)