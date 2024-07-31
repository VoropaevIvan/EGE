count_par = 4
n = 0
delay = 0


processes = {}
with open('files/22_d.csv') as f:
    f.readline()
    for s in f:
        id_, time, zav = s.strip().split(',')
        processes[int(id_)] = [int(time), [int(x) for x in zav.split(';')]]
        n += 1
print(processes)
otv = -1
print('Паралельно:', count_par)
print('Всего процессов:', n)
used = set()


def when_can_finish(pr_id, when_finish):
    global used
    used.add(pr_id)
    if pr_id in when_finish:
        return when_finish[pr_id]
    else:
        if processes[pr_id][1] == [0]:
            return -10000
        return processes[pr_id][0] + max(when_can_finish(x, when_finish) for x in processes[pr_id][1])


def rec(lines, when_finish):
    global otv
    global used
    otv = max(otv, min(lines))
    #print(when_finish, lines)
    if min(lines) == 8:
        print(when_finish)
    for i in range(count_par):
        if lines[i] == min(lines):
            for pr_id in range(1, n + 1):
                # take proc
                if pr_id not in when_finish:
                    used.clear()
                    time_can_start = when_can_finish(pr_id, when_finish) - processes[pr_id][0]
                    if time_can_start <= min(lines):
                        for time in range(max(time_can_start, min(lines)- delay), min(lines)+1):
                            #print(time)
                            if time + processes[pr_id][0] > min(lines):
                                lines_t, when_finish_t = list(lines), when_finish.copy()
                                lines_t[i] = time + processes[pr_id][0]
                                when_finish_t[pr_id] = time + processes[pr_id][0]
                                for pr_f in used:
                                    if pr_f not in when_finish_t:
                                        when_finish_t[pr_f] = -100000
                                # lines_t.sort()
                                rec(tuple(lines_t), when_finish_t.copy())
            break


rec(tuple([0] * count_par), {0: 0})
print(otv)
