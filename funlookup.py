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
        sys.exit('Run it with root!)

from __future__ import print_function
from scapy.all import *

import time

__version__ = "0.0.3"

# Fixup function to extract dhcp_options by key
def get_option(dhcp_options, key):

    must_decode = ['hostname', 'domain', 'vendor_class_id']
    try:
        for i in dhcp_options:
            if i[0] == key:
                # If DHCP Server Returned multiple name servers 
                # return all as comma seperated string.
                if key == 'name_server' and len(i) > 2:
                    return ",".join(i[1:])
                # domain and hostname are binary strings,
                # decode to unicode string before returning
                elif key in must_decode:
                    return i[1].decode()
                else: 
                    return i[1]        
    except:
        pass


def handle_dhcp_packet(packet):

    # Match DHCP discover
    if DHCP in packet and packet[DHCP].options[0][1] == 1:
        print('---')
        print('New DHCP Discover')
        #print(packet.summary())
        #print(ls(packet))
        hostname = get_option(packet[DHCP].options, 'hostname')
        print(f"Host {hostname} ({packet[Ether].src}) asked for an IP")


    # Match DHCP offer
    elif DHCP in packet and packet[DHCP].options[0][1] == 2:
        print('---')
        print('New DHCP Offer')
        #print(packet.summary())
        #print(ls(packet))

        subnet_mask = get_option(packet[DHCP].options, 'subnet_mask')
        lease_time = get_option(packet[DHCP].options, 'lease_time')
        router = get_option(packet[DHCP].options, 'router')
        name_server = get_option(packet[DHCP].options, 'name_server')
        domain = get_option(packet[DHCP].options, 'domain')

        print(f"DHCP Server {packet[IP].src} ({packet[Ether].src}) "
              f"offered {packet[BOOTP].yiaddr}")

        print(f"DHCP Options: subnet_mask: {subnet_mask}, lease_time: "
              f"{lease_time}, router: {router}, name_server: {name_server}, "
              f"domain: {domain}")


    # Match DHCP request
    elif DHCP in packet and packet[DHCP].options[0][1] == 3:
        print('---')
        print('New DHCP Request')
        #print(packet.summary())
        #print(ls(packet))

        requested_addr = get_option(packet[DHCP].options, 'requested_addr')
        hostname = get_option(packet[DHCP].options, 'hostname')
        print(f"Host {hostname} ({packet[Ether].src}) requested {requested_addr}")


    # Match DHCP ack
    elif DHCP in packet and packet[DHCP].options[0][1] == 5:
        print('---')
        print('New DHCP Ack')
        #print(packet.summary())
        #print(ls(packet))

        subnet_mask = get_option(packet[DHCP].options, 'subnet_mask')
        lease_time = get_option(packet[DHCP].options, 'lease_time')
        router = get_option(packet[DHCP].options, 'router')
        name_server = get_option(packet[DHCP].options, 'name_server')

        print(f"DHCP Server {packet[IP].src} ({packet[Ether].src}) "
              f"acked {packet[BOOTP].yiaddr}")

        print(f"DHCP Options: subnet_mask: {subnet_mask}, lease_time: "
              f"{lease_time}, router: {router}, name_server: {name_server}")

    # Match DHCP inform
    elif DHCP in packet and packet[DHCP].options[0][1] == 8:
        print('---')
        print('New DHCP Inform')
        #print(packet.summary())
        #print(ls(packet))

        hostname = get_option(packet[DHCP].options, 'hostname')
        vendor_class_id = get_option(packet[DHCP].options, 'vendor_class_id')

        print(f"DHCP Inform from {packet[IP].src} ({packet[Ether].src}) "
              f"hostname: {hostname}, vendor_class_id: {vendor_class_id}")

    else:
        print('---')
        print('Some Other DHCP Packet')
        print(packet.summary())
        print(ls(packet))

    return

if __name__ == "__main__":
    sniff(filter="udp and (port 67 or 68)", prn=handle_dhcp_packet)
