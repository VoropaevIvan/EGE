from ipaddress import *
print(bin(int(ip_address('255.255.255.240')))[2:])
print(bin(int(ip_address('192.168.106.35')))[2:])
print(bin(int(ip_address('192.168.106.117')))[2:])

net = ip_network('192.168.32.160/28')
count_uzl = len(list(net.hosts()))
count_ip = len(list(net))
print(count_ip, count_uzl)