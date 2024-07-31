count_par = 1
n = 0


processes = {}
with open('files/22-2.csv') as f:
    f.readline()
    for s in f:
        id_, time, zav = s.strip().split(',')
        processes[int(id_)] = [int(time), [int(x) for x in zav.split(';')]]
        n += 1
print(processes)
otv = -1
count_f = 0
from functools import lru_cache
a_q = []
#@lru_cache(None)
def rec(lines, wait, when_finish):
    global count_f
    count_f +=1
    global otv
    otv = max(otv, min(lines))
    #print(otv)
    a_q.append((lines, wait, when_finish))
    f = 1
    while f:
        f = 0
        for i in range(1, n + 1):
            if all(i != x[0] for x in wait):
                if i not in when_finish:
                    if all(z in when_finish and when_finish[z] <= min(lines) for z in processes[i][1]):
                        wait.add((i, max(when_finish[z] for z in processes[i][1])))
                        f = 1

    if not wait:
        return
    #print(lines, wait, when_finish)

    for i in range(count_par):
        if lines[i] == min(lines):
            for pr, t_start in wait:
                # take
                if t_start <= min(lines):
                    # choose time to start
                    for v in range(t_start, min(lines) + 1):
                        if v + processes[pr][0] <= min(lines):
                            continue
                        when_finish_t = when_finish.copy()
                        wait_t = wait.copy()
                        lines_t = list(lines)

                        when_finish_t[pr] = lines_t[i] + processes[pr][0]
                        lines_t[i] = lines_t[i] + processes[pr][0]
                        wait_t.remove([x for x in wait if x[0] == pr][0])

                        rec(tuple(lines_t), wait_t, when_finish_t)
                # skip
                when_finish_t = when_finish.copy()
                wait_t = wait.copy()
                if all(when_finish[x] == 0 for x in processes[pr][1]):
                    when_finish_t[pr] = 0
                    wait_t.remove([x for x in wait if x[0] == pr][0])
                else:
                    when_finish_t[pr] = processes[pr][0] + max(when_finish[x] for x in processes[pr][1])
                    wait_t.remove([x for x in wait if x[0] == pr][0])
                rec(lines, wait_t, when_finish_t)


            break


rec(tuple([0]*count_par), set(), {0: 0})
print(otv)
print(count_f)
