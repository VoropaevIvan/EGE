with open('ege2023.txt') as file:
    s = file.readline().strip()
#s = '+1+22+++++1+121313131'
# Рассматриваем каждый новый символ
cur_len = 0
is_pred_plus = 0
is_plus_in = 0
ans = -1
for i in range(len(s)):
    if s[i] == '+':
        is_plus_in = 1
        if is_pred_plus == 1 or cur_len == 0:
            is_plus_in = 0
            cur_len = 0
            is_pred_plus = 0
        else:
            is_pred_plus = 1
            cur_len += 1
    else:
        is_pred_plus = 0
        cur_len += 1
        if is_plus_in:
            ans = max(ans, cur_len)
print(ans)