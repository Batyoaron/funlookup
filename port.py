import pyfiglet
import os
import time
print("\033[1;33;40m \n")
ascii_banner = pyfiglet.figlet_format("funlookup")
print(ascii_banner)
print("\033[1;31;40m \n")
print('                                 [by]: Batyoaron')
print("\033[1;32;40m \n")
print('port')

print("\033[1;31;40m \n")
print('this will take a few minutes')
print('')
print("\033[1;32;40m \n")
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




from socket import *
import time
startTime = time.time()

if __name__ == '__main__':
   target = input('Enter the host to be scanned: ')
   t_IP = gethostbyname(target)
   print ('Starting scan on host: ', t_IP)
   
   for i in range(50, 500):
      s = socket(AF_INET, SOCK_STREAM)
      
      conn = s.connect_ex((t_IP, i))
      if(conn == 0) :
         print ('Port %d: OPEN' % (i,))
      s.close()
print('Time taken:', time.time() - startTime)
