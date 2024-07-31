from ipaddress import *

for i in range(0, 32 + 1):
    net_1 = ip_network(f'120.91.85.213/{i}', 0)
    net_2 = ip_network(f'120.91.89.205/{i}', 0)
    if net_1 == net_2:
        print(net_1.netmask)