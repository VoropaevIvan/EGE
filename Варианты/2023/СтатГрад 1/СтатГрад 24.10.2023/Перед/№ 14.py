otv = []
for x in range(36 + 1):
    for y in range(36 + 1):
        a = 1*37**7 + \
            2*37**6 + \
            x*37**5 + \
            6*37**4 + \
            4*37**3 + \
            3*37**2 + \
            y*37**1 + \
            7*37**0
        if a % 36 == 0:
            otv.append(y*37 + x)
print(max(otv))
