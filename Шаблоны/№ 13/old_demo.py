# Для узла с IP-адресом 111.81.27.224 адрес сети равен 111.81.27.192. Чему
# равен последний (самый правый) байт маски? Ответ запишите в виде
# десятичного числа.

from ipaddress import *

for i in range(0, 32 + 1):
    net_s = '111.81.27.192/' + str(i)
    ip_net = ip_network(net_s, 0)
    if str(ip_net) == net_s:
        if ip_address('111.81.27.224') in ip_net:
            print(ip_net.netmask)


from ipaddress import *

for i in range(0, 32 + 1):
    try:
        net = ip_network('111.81.27.192/' + str(i))
        if ip_address('111.81.27.224') in net:
            print(net.netmask)
    except:
        pass