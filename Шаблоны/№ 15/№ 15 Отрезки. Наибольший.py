A = 1
f_usl = 1
for x in [k * 0.25 for k in range(-10_000, 10_000)]:
    P = 5 <= x <= 30
    Q = 14 <= x <= 23
    f = (P == Q) <= (not A)
    if f == f_usl:
        print(x)




# exit()
# otvet = max(otv) - min(otv)
# print(otvet)
# print(len(otv) == otvet * 4 + 1)
# sum_ = 0
# otv.append(10000)
# for i in range(1, len(otv)):
#     if otv[i] - otv[i-1] > 0.25:
#         print(sum_)
#         sum_ = 0
#     else:
#         sum_ += 0.25
#
#
# A = 1
# f_usl = 1
# otv = set()
# for x in [k * 0.25 for k in range(-10_000, 10_000)]:
#     P = 9 <= x <= 19
#     Q = 24 <= x <= 54
#     R = 28 <= x <= 43
#     f = A <= (P or Q)
#     if f == f_usl:
#         otv.add(x)
#
# print(otv)
#
# otvet = max(otv) - min(otv)
# print(otvet)
# print(len(otv) == otvet * 4 + 1)










# st = {x for x in [k * 0.25 for k in range(int(min(otv)*4), int(max(otv)*4)+1)]}
# print(st)
# #st-=otv
# print(sorted(st - otv))