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

print('my data')
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
print('')
print('')
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
print('your ip:')
print(s.getsockname()[0])
print("\033[1;34;40m \n")
print('hint: if you disconnect from your wifi you get your real ip')
print("\033[1;32;40m \n")

print('')
print('proxy:')
import requests

proxy_ip = "<IP>"
proxy_port = "<PORT>"
proxy_user = "<USERNAME>"
proxy_pass = "<PASSWORD>"

proxies = {
    "http": f"http://{proxy_user}:{proxy_pass}@{proxy_ip}:{proxy_port}/",
    "https": f"http://{proxy_user}:{proxy_pass}@{proxy_ip}:{proxy_port}/"
}

url = 'https://api.ipify.org'

try:
    response = requests.get(url, proxies=proxies)
    assert response.text==proxy_ip
except:
    print("Proxy does not work")
