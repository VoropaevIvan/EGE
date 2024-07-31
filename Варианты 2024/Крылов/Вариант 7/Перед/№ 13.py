from ipaddress import *

def check(net):
    for ip in net:
        ip_2 = bin(int(ip))[2:]
        if not (ip_2[:16].count('1') >= ip_2[16:].count('1')):
            return 0
    return 1

for A in range(256):
    try:
        net = ip_network(f'255.211.33.160/255.255.{A}.0', 0)
        if check(net) == 1:
            print(A)
    except:
        ...

