from ipaddress import *

for i in range(0, 33):
    try:
        if ip_address('44.44.229.28') in ip_network(f'44.44.224.0/{i}'):
            print(i)
    except:
        ...
