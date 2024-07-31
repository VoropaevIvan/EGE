with open('27_B.txt', 'r') as f_in, open('27_b_filter.txt', 'w') as f_out:
    for i, s in enumerate(f_in):
        s = s.strip()
        if int(s) > 10_000:
            print(i, s, file=f_out)
