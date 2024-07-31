from ipaddress import *

for ip in ip_network('136.36.240.16/255.255.255.248'):
    if '101' not in bin(int(ip))[2:].zfill(32):
        print(ip)