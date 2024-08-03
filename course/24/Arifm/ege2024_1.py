with open('ege2024_1.txt') as file:
    s = file.readline().strip()
#s = '07*7'
is_znak_in = 0
cur_len = 0
is_pred_znak = 0
ans = -1
for i in range(len(s)):
    cur_len += 1
    if s[i] in '*-':
        if cur_len == 1 or is_pred_znak == 1:
            is_znak_in = 0
            is_pred_znak = 0
            cur_len = 0
        else:
            is_znak_in = 1
            is_pred_znak = 1

    if s[i] in '0789':
        if s[i] == '0':
            if is_pred_znak == 1 or cur_len == 1:
                is_znak_in = 0
                cur_len = 0
        if is_znak_in == 1:
            print(s[i-cur_len+1:i+1])
            ans = max(ans, cur_len)
        is_pred_znak = 0
print(ans)
