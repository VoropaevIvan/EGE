A = 0
for x in [k*0.25 for k in range(10_000)]:
    P = 3 <= x <= 43
    Q = 18 <= x <= 91
    R = 72 <= x <= 115
    f = Q <= ((not P) <= (((not R) and (not A)) <= (not Q)))
    if f != 1:
        print(x)
#(x ∈ Q) → (¬(x ∈ P) → ((¬(x ∈ R) ∧ ¬(x ∈ A)) → ¬(x ∈ Q)))