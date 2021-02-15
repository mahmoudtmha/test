import os
import time
import string
import random
import requests
from colorama import Fore
from colorama import init
import sys
from multiprocessing.dummy import Pool as ThreadPool
init(autoreset=True)
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def ipRange(start_ip, end_ip):
    start = list(map(int, start_ip.split(".")))
    end = list(map(int, end_ip.split(".")))
    temp = start
    ip_range = []

    ip_range.append(start_ip)
    while temp != end:
        start[3] += 1
        for i in (3, 2, 1):
            if temp[i] == 256:
                temp[i] = 0
                temp[i - 1] += 1
        ip_range.append(".".join(map(str, temp)))

    return ip_range

for i in open(sys.argv[1], 'r'):
    range = i.strip()
    start_ip, end_ip = range.split(':')
    ipRange(start_ip, end_ip)
    ip_range = ipRange(start_ip, end_ip)
    for ip in ip_range:
        print(ip)
        open("IPS.txt", "a").write(ip + "\n")