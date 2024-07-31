from ipaddress import *

for i in range(0, 33):
    try:
        net = ip_network(f'244.55.138.96/{i}')
        if ip_address('244.55.138.100') in ip_network(f'244.55.138.96/{i}'):
            print(net.netmask)
    except:
        ...
