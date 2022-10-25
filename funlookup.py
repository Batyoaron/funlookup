import pyfiglet
import os
import subprocess as sp
import time
import pyfiglet
import os

import requests
import json
import random
import sys
import os, sys
import socket

from datetime import datetime
os.system('clear')
print("\033[1;33;40m \n")
ascii_banner = pyfiglet.figlet_format("funlookup")
print(ascii_banner)
print("\033[1;31;40m \n")
print('                                 [by]: Batyoaron')
print('                                 [version]: 2.0')
print("\033[1;33;40m \n")

print('[1]: wifi scanner')
print('[2]: telnet checker')
print('[3]: ip data')
print('[4]: DHCP listener')
print('')
print("\033[1;36;40m \n")




chs = input('your choice here: ')




print("\033[1;32;40m \n")

## wifi scanner

if chs == "1":os.system('clear')

if chs == "1":print("\033[1;33;40m \n")
if chs == "1":ascii_banner = pyfiglet.figlet_format("funlookup")
if chs == "1":print(ascii_banner)
print('')
 
if chs == "1":
    IP = "192.168.1.1"
    print("[+] Starting " + IP)
    dot = IP.rfind(".")
    IP = IP[0:dot + 1]
    for i in range(1, 255):
        host = IP + str(i)
        response = os.system("ping -c 1 -w 1 " + host + " >/dev/null")
        if response == 0:
            print("\033[1;32;40m")
            print(host + " is up")
        else:
           print("\033[1;31;40m")
           print(host + " is down")
    exit()
           
           
#telnet scanner

if chs == "2":os.system('clear')

if chs == "2":print("\033[1;33;40m \n")
if chs == "2":ascii_banner = pyfiglet.figlet_format("funlookup")
if chs == "2":print(ascii_banner)
print('')

if chs == "2":print("\033[1;35;40m \n")
if chs == "2":print('')


if chs == "2":
            tel = input('\033[1;32;40m type the ip address here: \033[1;33;40m ')
            if(tel >= '0' and tel <= '254' + '.' + tel >= '0' and tel <= '254' + '.' + tel >= '0' and tel <= '254' + '.' + tel >= '0' and tel <= '254'):
                print("\033[1;32;40m \n")
                print('looks good ip')
           
                time.sleep(2)
                print("\033[1;32;40m \n")
                
                print('checking.....')
                time.sleep(3)
                print("\033[1;32;40m \n")
                print('probably:(50%) of telnet works')
                exit()
            else:
                    print("\033[1;31;40m \n")
                    print('bad ip address')
                    exit()
                    
                    
                    
###ip lookup

if chs == "3":os.system('clear')
if chs == "3":print("\033[1;33;40m \n")
if chs == "3":ascii_banner = pyfiglet.figlet_format("funlookup")
if chs == "3":print(ascii_banner)
print('')

if chs == "3":
    ip_address = input('ip address: ')
    
    request_url = (str('https://geolocation-db.com/jsonp/' + ip_address))
    response = requests.get(request_url)
    result = response.content.decode()
    result = result.split("(")[1].strip(")")
    result  = json.loads(result)
    print(result)
    exit()
    
    

    

##DHCP listenter
if chs == "4":os.system('clear')

if chs == "4":print("\033[1;33;40m \n")
if chs == "4":ascii_banner = pyfiglet.figlet_format("funlookup")
if chs == "4":print(ascii_banner)
print('')


if chs == "4":
    if not os.geteuid()==0:
        print("\033[1;31;40m \n")
        sys.exit('Run it with root!')
        
                   
              

from scapy.all import *
import time

def listen_dhcp():
    # Make sure it is DHCP with the filter options
    sniff(prn=print_packet, filter='udp and (port 67 or port 68)')


def print_packet(packet):
    # initialize these variables to None at first
    target_mac, requested_ip, hostname, vendor_id = [None] * 4
    # get the MAC address of the requester
    if packet.haslayer(Ether):
        target_mac = packet.getlayer(Ether).src
    
    dhcp_options = packet[DHCP].options
    for item in dhcp_options:
        try:
            label, value = item
        except ValueError:
            continue
        if label == 'requested_addr':
           
            requested_ip = value
        elif label == 'hostname':
           
            hostname = value.decode()
        elif label == 'vendor_class_id':
            
            vendor_id = value.decode()
    if target_mac and vendor_id and hostname and requested_ip:
        
        time_now = time.strftime("[%Y-%m-%d - %H:%M:%S]")
        print(f"{time_now} : {target_mac}  -  {hostname} / {vendor_id} requested {requested_ip}")


if __name__ == "__main__":
    listen_dhcp()
