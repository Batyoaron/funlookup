import pyfiglet
import os
import time
os.system('clear')
print("\033[1;33;40m \n")
ascii_banner = pyfiglet.figlet_format("funlookup")
print(ascii_banner)
print("\033[1;31;40m \n")
print('                                 [by]: Batyoaron')
print("\033[1;32;40m \n")

print('ping')
print('')
print('')
print('press "enter" to start')
print('')
answer = input()
os.system('clear')
time.sleep(3)
print("\033[1;33;40m \n")
ascii_banner = pyfiglet.figlet_format("funlookup")
print(ascii_banner)
print("\033[1;32;40m \n")
time.sleep(2)
print('please wait...')
time.sleep(5)
print('')
print('')
print("\033[1;34;40m \n")

import os
 
IP = input("[+] Enter Host IP Address:\t")
print("[+] Starting " + IP)
dot = IP.rfind(".")
IP = IP[0:dot + 1]

for i in range(1, 255):
    host = IP + str(i)
    response = os.system("ping -c 1 -w 1 " + host + " >/dev/null")
 
    if response == 0:
        print(host + " is up")
    else:
        print(host + " is down")
