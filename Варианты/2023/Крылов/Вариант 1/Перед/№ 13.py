from ipaddress import *

count = 0
for ip in ip_network('142.108.56.118/255.255.255.240', 0):
    ip_2 = bin(int(ip))[2:]
    if ip_2[:16].count('1') < ip_2[16:].count('1'):
        count += 1
print(count)