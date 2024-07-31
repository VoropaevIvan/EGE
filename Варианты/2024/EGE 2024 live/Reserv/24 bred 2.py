with open('24_17616.txt') as file:
    s = file.readline().strip()
answers = []
for L in range(len(s)):
    cur = ''
    if s[L] in '0123456789':
        for R in range(L, len(s)):
            cur = cur + s[R]
            if ('++' in cur) or ('**' in cur) or ('+*' in cur) or ('*+' in cur):
                break
            try:
                res = eval(cur)
                if res == 0:
                    answers.append(cur)
            except:
                ...
answers.sort(key=len, reverse=True)
print(answers[:50])
print(len(answers[0]))
