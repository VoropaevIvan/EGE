ok_R = []
for N in range(1, 200):
    N_2 = bin(N)[2:]
    if N % 3 == 0:
        R_2 = N_2.replace('0', '11')
    else:
        R_2 = N_2.replace('1', '10')
    R = int(R_2, 2)
    if R <= 161:
        ok_R.append(R)
print(max(ok_R))