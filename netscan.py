#!/usr/bin/python3

import os
import subprocess
import sys

# Options
rdr = False #reverse-domain-resolution

privateIP = (subprocess.check_output("hostname -I", shell=True).decode('ascii'))[:-1]
privateGatewayIP = (subprocess.check_output("ip route | grep default | awk '{print $3}'", shell=True).decode('ascii'))[:-1]
publicGatewayIP = (subprocess.check_output("dig +short myip.opendns.com @resolver1.opendns.com", shell=True).decode('ascii'))[:-1]
rdrResults = None

if(len(sys.argv) > 1):
    for x in sys.argv:
        if(x == '-rdr'):
            rdr = True
            subprocess.check_output("nmap -sL " + privateGatewayIP + "/24 > .rdr.txt", shell=True)

print("Private IP: ", privateIP)
print("Private Gateway IP: ", privateGatewayIP);
print("Public Gateway IP: ", publicGatewayIP)

if(rdr):
    os.system("cat .rdr.txt | awk {'if(substr($5, 1, 3) != 192) print $5, $6'}")
