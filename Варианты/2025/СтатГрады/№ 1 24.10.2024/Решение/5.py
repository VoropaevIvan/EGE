n = 567_891_233
n_2 = bin(n)[2:]
R = int('1'+n_2+'10', 2)
print(R)
ans = []
for N in range(567_891_234, 567_891_234-1000, -1):
    if N % 2 == 0:
        n_2 = '11' + bin(N)[2:]
    else:
        n_2 = '1' + bin(N)[2:] + '10'
    r = int(n_2, 2)
    ans.append(r)
print(max(ans))