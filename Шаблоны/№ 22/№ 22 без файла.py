from functools import lru_cache
import json

count_par = 4
n = 14
delay = -1

count_iter = 0
processes = {}
for i in range(n):
    s = input()
    id_, time, zav = s.strip().split('\t')
    processes[int(id_)] = [int(time), [int(x) for x in zav.split(';')]]


print(processes)
otv = -1
print('Паралельно:', count_par)
print('Всего процессов:', n)
used = set()

#@lru_cache(None)
def when_can_finish(pr_id, when_finish):
    when_finish = json.loads(when_finish)
    when_finish = {int(x): when_finish[x] for x in sorted(when_finish)}

    global used
    used.add(pr_id)
    if pr_id in when_finish:
        return when_finish[pr_id]
    else:
        if processes[pr_id][1] == [0]:
            return -10000
        return processes[pr_id][0] + max(when_can_finish(x, json.dumps(when_finish)) for x in processes[pr_id][1])




@lru_cache(None)
def rec(lines, when_finish):
    global count_iter
    global delay
    count_iter += 1
    when_finish = json.loads(when_finish)
    when_finish = {int(x): when_finish[x] for x in sorted(when_finish)}
    global otv
    global used
    otv = max(otv, min(lines))
    #print(when_finish, lines)
    # if min(lines) == 12:
    #     print(lines, when_finish)
    #print(lines, when_finish)
    for i in range(count_par):
        if lines[i] == min(lines):
            for pr_id in range(1, n + 1):
                # take proc
                if pr_id not in when_finish:
                    used.clear()
                    time_can_start = when_can_finish(pr_id, json.dumps(when_finish)) - processes[pr_id][0]
                    used_t = used.copy()
                    if time_can_start <= min(lines):
                        for time in range(max(time_can_start, min(lines)-processes[pr_id][0] if delay == -1 else min(lines)-delay), min(lines) + 1):
                            # print(time)
                            #time = min(lines)
                            if time + processes[pr_id][0] > min(lines):
                                lines_t, when_finish_t = list(lines), when_finish.copy()
                                lines_t[i] = time + processes[pr_id][0]
                                when_finish_t[pr_id] = time + processes[pr_id][0]
                                for pr_f in used_t:
                                    if pr_f not in when_finish_t:
                                        when_finish_t[pr_f] = -100000
                                lines_t.sort()
                                when_finish_t = {int(x): when_finish_t[x] for x in sorted(when_finish_t)}
                                rec(tuple(lines_t), json.dumps(when_finish_t))
            break


rec(tuple([0] * count_par), json.dumps({0: 0}))
print('Ответ:', otv)
print(rec.cache_info())
print(count_iter)