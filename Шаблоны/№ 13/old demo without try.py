# Для узла с IP-адресом 57.179.208.27 адрес сети равен 57.179.192.0. Каково
# наибольшее возможное количество единиц в разрядах маски?

from ipaddress import *

for i in range(0, 32 + 1):
    net_s = '57.179.192.0/' + str(i)
    ip_net = ip_network(net_s, 0)
    if str(ip_net) == net_s:
        if ip_address('57.179.208.27') in ip_net:
            print(bin(int(ip_net.netmask))[2:].count('1'))


from ipaddress import *

for i in range(0, 32 + 1):
    try:
        net = ip_network('57.179.192.0/' + str(i))
        if ip_address('57.179.208.27') in net:
            print(i)
    except:
        pass
