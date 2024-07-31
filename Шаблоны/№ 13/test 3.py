from ipaddress import *

print(bin(int(ip_address('111.81.208.27')))[2:])
print(bin(int(ip_address('111.81.192.0')))[2:])
if ip_address('111.81.208.27') in ip_network('111.81.208.27/30', 0):
    print('Принадлежит')
else:
    print('Не принадлежит')

if ip_address('111.81.208.27') in ip_network('111.81.208.27/30', 0).hosts():
    print('Принадлежит')
else:
    print('Не принадлежит')
