# file = open('24.txt')
# s = file.readline()
s = '+068*7--8-*-08*6*6*6*6*0'
s = '78-8'
s = '+' + s + '+' # добавляем к строке мусорные символы, чтобы смотреть на s[i-1] и s[i+1]
t = 0
ans = -1
flag = 0 # наличие корректного знака (между ненулевыми цифрами)
for i in range(1, len(s)):
    if s[i] in '678':
        t += 1
    elif s[i] == '0':
        if s[i-1] in '678' and s[i+1] in '678':
            t+=1
        else:
            t = 0
            flag = 0
    elif s[i] in '-*':
        if s[i-1] in '678' and s[i+1] in '678':
            t+=1
            flag = 1
        else:
            t = 0
            flag = 0
    if flag == 1:
        ans = max(ans, t)
print(ans)


