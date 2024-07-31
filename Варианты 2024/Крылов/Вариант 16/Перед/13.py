from ipaddress import *

for i in range(0, 33):
    try:
        if ip_address('244.55.229.28') in ip_network(f'244.0.0.0/{i}'):
            print(32 - i)
    except:
        ...
