otv = []
for x in range(37):
    for y in range(37):
        a = 2*37**7 + 1*37**6 + x*37**5 + 4*37**4 + 5*37**3 + 7*37**2 + y*37**1 + 9*37**0
        if a % 36 == 0:
            otv.append(x*37 + y)
print(max(otv))

# 21x457y9