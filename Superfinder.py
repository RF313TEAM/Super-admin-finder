import requests as re1
import os
import threading
from colorama import Fore,Back
#os.system("clear")
print(Fore.YELLOW+'''
      
      
      
    █▀▀ ░█─░█ ░█▀▀█ ░█▀▀▀ ░█▀▀█ 　 █▀▀ ▀█▀ ░█▄─░█ ░█▀▀▄ ░█▀▀▀ ░█▀▀█ 
    ▀▀█ ░█─░█ ░█▄▄█ ░█▀▀▀ ░█▄▄▀ 　 █▀▀ ░█─ ░█░█░█ ░█─░█ ░█▀▀▀ ░█▄▄▀ 
    ▀▀▀ ─▀▄▄▀ ░█─── ░█▄▄▄ ░█─░█ 　 ▀── ▄█▄ ░█──▀█ ░█▄▄▀ ░█▄▄▄ ░█─░█
        
'''+Fore.GREEN+'''
    🆂🆄🅿🅴🆁 🅵🅸🅽🅳🅴🆁
    Coded BY Abdalmahdi && The ALien Team'''+Fore.RED+'''
    tele:t.me/FAD_Hack
''')
dirs=open("wordlist.txt","r").read().splitlines()
url=input("Enter The ("+Fore.RED+"site"+Fore.WHITE+"):")
def spa(dir):
    try:
        
        req1=re1.get(url+"/"+dir)
        if req1.status_code==200:
            print(Fore.BLUE+" [+] "+Fore.WHITE+url+"/"+dir+Fore.GREEN+" Found["+Fore.RED+"200"+Fore.GREEN+"]")
            exit()
        else:
            print(Fore.BLUE+" [+] "+Fore.WHITE+url+"/"+dir+Fore.RED+" Not Found["+Fore.YELLOW+str(req1.status_code)+Fore.RED+"]")
    except:
       print(Fore.BLUE+" [+] "+Fore.WHITE+url+"/"+dir+Fore.YELLOW+" [Timeout!!]")
threads=[]
for dir in dirs:
    t1=threading.Thread(target=spa,args=(dir,))
    t1.start()
    threads.append(t1)
for thread in threads:
    thread.join()
