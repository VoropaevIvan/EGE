from ipaddress import *

def check(net):
    for ip in net:
        ip_2 = bin(int(ip))[2:]
        if not(ip_2[16:].count('1') > 3):
            return 0
    return 1

for A in range(256):
    try:
        net = ip_network(f'183.192.{A}.0/255.255.252.0')
        if check(net) == 1:
            print(A)
    except:
        ...

