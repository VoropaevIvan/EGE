from ipaddress import *
st = set()
for i in range(0, 32 + 1):
    net_s = '125.28.160.0/' + str(i)
    ip_net = ip_network(net_s, 0)
    if str(ip_net) == net_s:
        if ip_address('125.28.160.73') in ip_net:
            if len(list(ip_net.hosts())) >= 500:
                st.add(str(ip_net.netmask).split('.')[2])

print(len(st))
