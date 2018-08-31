import os
import ast
import time
import subprocess

while(True):
    print('Checking internet...')
    hostname = "www.google.com"
    response = subprocess.call("ping {}".format(hostname), shell=True)
    if response == 0:
        print("""
=======================
Internet is functional!
=======================
            """)
    else:
        print("""
===========================
Internet is down! Fixing...
===========================
            """)
        subprocess.call('ipconfig /release', shell=True)
        subprocess.call('ipconfig /renew', shell=True)
    for i in range(1,15+1):
        print((15+1)-i)
        time.sleep(1)
    subprocess.call('cls', shell=True)
    
    




    
    
