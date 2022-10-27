import pyfiglet
import os
import subprocess as sp
import time
import pyfiglet
import os
import atexit
import urllib.request
from pystyle import *

import requests
import json
import random
import sys
import os, sys
import socket
import pystyle
from datetime import datetime
os.system('clear')


Write.Print("[+] Welcome to funlookup", Colors.blue_to_red, interval=0.1)

print('')
print("\033[1;35;40m \n")
atexit.register(print, '[%] Thanks for used funlookup')
   
    
url = "http://www.google.com"
timeout = 5
try:
	request = requests.get(url, timeout=timeout)
	print("\033[1;32;40m \n")
    
	print("looks good")
except (requests.ConnectionError, requests.Timeout) as exception:
	
	count = 0
	while(count < 5900000):
	   count = count +1
	   print("\033[1;33;40m \n")
	   ascii_banner = pyfiglet.figlet_format("funlookup")
	   print(ascii_banner)
	   print("\033[1;31;40m \n")
	   print("o o... it looks like you are in offline mode")
	   time.sleep(1)
	   
	   
	   os.system('clear')
	   print("\033[1;33;40m \n")
	   ascii_banner = pyfiglet.figlet_format("funl--kup")
	   print(ascii_banner)
	   print("\033[1;31;40m \n")
	   print("o o... it looks like you are in offline mode")
	   time.sleep(0.1)
	   os.system('clear')
	   
	   print("\033[1;33;40m \n")
	   ascii_banner = pyfiglet.figlet_format("funlookup")
	   print(ascii_banner)
	   print("\033[1;31;40m \n")
	   print("o o... it looks like you are in offline mode")
	   time.sleep(1)
	   os.system('clear')


external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')

os.system('clear')
print("\033[1;33;40m \n")
ascii_banner = pyfiglet.figlet_format("funlookup")
print(ascii_banner)
print("\033[1;31;40m \n")
print('                                 [by]: Batyoaron')
print('                                 [version]: 2.1')
print("\033[1;33;40m \n")
print('')

print('[1]: Wifi scanner          [5]: My data')
print('[2]: Telnet checker        \033[1;34;40m[6]: Coming soon...\033[1;33;40m')
print('[3]: Ip data             \033[1;34;40m  [7]: Coming soon...\033[1;33;40m')
print('[4]: DHCP listener\033[1;31;40m(root)   \033[1;34;40m[8]: Coming soon...')
print('')
print('')
print('\033[1;30;40m[ press\033[1;31;40m X\033[1;30;40m to exit ]')
print("\033[1;36;40m \n")




chs = input('your choice here: ')

if chs == "x":exit()
if chs == "X":exit()

if(chs <= '0'):
    print("\033[1;31;40m \n")
    print('Wrong choice')
    os.execl(sys.executable, sys.executable, *sys.argv)
    
    
if(chs >= '6'):
    print("\033[1;31;40m \n")
    print('Wrong choice')
    os.execl(sys.executable, sys.executable, *sys.argv)



## wifi scanner

if chs == "1":os.system('clear')

if chs == "1":print("\033[1;33;40m \n")
if chs == "1":ascii_banner = pyfiglet.figlet_format("funlookup")
if chs == "1":print(ascii_banner)
if chs == "1":
    print("\033[1;36;40m \n")
    print('[TIP]: if 192.168.1.1 is down you need to connect to the router')
print('')
print("\033[1;33;40m \n")
 
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
                print('')
                op = input('\033[1;36;40mpress \033[1;32;40mENTER\033[1;36;40m to continue or \033[1;31;40mX\033[1;36;40m to exit: ')
                if op == "":os.execl(sys.executable, sys.executable, *sys.argv)
                if op == "x":exit()

            else:
                    print("\033[1;31;40m \n")
                    print('bad ip address')
                    os.execl(sys.executable, sys.executable, *sys.argv)



                    
                    
                    
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
    print("\033[1;31;40m \n")
    
    op = input('\033[1;36;40mpress \033[1;32;40mENTER\033[1;36;40m to continue or \033[1;31;40mX\033[1;36;40m to exit: ')
    if op == "":os.execl(sys.executable, sys.executable, *sys.argv)
    if op == "x":exit()



    
    
##my data 5



if chs == "5":
    os.system('clear')
if chs == "5":print("\033[1;33;40m \n")
if chs == "5":ascii_banner = pyfiglet.figlet_format("funlookup")
if chs == "5":print(ascii_banner)
print("\033[1;32;40m \n")
if chs == "5":print('')

if chs == "5":print('my ipv6: ' + external_ip)
if chs == "5":print('')

if chs == "5":
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    print('my private ip: ' + s.getsockname()[0])
    s.close()
    print('')
    
    op = input('\033[1;36;40mpress \033[1;32;40mENTER\033[1;36;40m to continue or \033[1;31;40mX\033[1;36;40m to exit: ')
    if op == "":os.execl(sys.executable, sys.executable, *sys.argv)
    if op == "x":
        exit()
    else:
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
        
if chs == "4":
    from pystyle import *
    Write.Print("[+] DHCP listener started. Please wait...", Colors.blue_to_purple, interval=0.1)
        
                   
              
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
    # get the DHCP options
    dhcp_options = packet[DHCP].options
    for item in dhcp_options:
        try:
            label, value = item
        except ValueError:
            continue
        if label == 'requested_addr':
            # get the requested IP
            requested_ip = value
        elif label == 'hostname':
            # get the hostname of the device
            hostname = value.decode()
        elif label == 'vendor_class_id':
            # get the vendor ID
            vendor_id = value.decode()
    if target_mac and vendor_id and hostname and requested_ip:
        # if all variables are not None, print the device details
        time_now = time.strftime("[%Y-%m-%d - %H:%M:%S]")
        print(f"{time_now} : {target_mac}  -  {hostname} / {vendor_id} requested {requested_ip}")


if __name__ == "__main__":
    listen_dhcp()






