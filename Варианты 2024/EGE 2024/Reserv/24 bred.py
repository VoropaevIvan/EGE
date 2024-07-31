with open('24_17616.txt') as file:
    s = file.readline().strip()

for x in ['++', '**', '+*', '*+']:
    s = s.replace(x, ' ')

answers = []
for x in s.split():
    for L in range(len(x)):
        for R in range(L, len(x)):
            cur = s[L:R+1]
            try:
                res = eval(cur)
                if res == 0:
                    answers.append(cur)
            except:
                ...
answers.sort(key=len, reverse=True)
print(answers[:50])
print(len(answers[0]))
