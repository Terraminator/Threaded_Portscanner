import pslib
import socket
import sys
import threading
from time import sleep
from datetime import datetime
import os

def banner():
	os.system("color a")
	print(r"""\
.______     ______   .______     .___________.    _______.  ______     ___      .__   __. .__   __.  _______ .______      
|   _  \   /  __  \  |   _  \    |           |   /       | /      |   /   \     |  \ |  | |  \ |  | |   ____||   _  \     
|  |_)  | |  |  |  | |  |_)  |   `---|  |----`  |   (----`|  ,----'  /  ^  \    |   \|  | |   \|  | |  |__   |  |_)  |    
|   ___/  |  |  |  | |      /        |  |        \   \    |  |      /  /_\  \   |  . `  | |  . `  | |   __|  |      /     
|  |      |  `--'  | |  |\  \----.   |  |    .----)   |   |  `----./  _____  \  |  |\   | |  |\   | |  |____ |  |\  \----.
| _|       \______/  | _| `._____|   |__|    |_______/     \______/__/     \__\ |__| \__| |__| \__| |_______|| _| `._____|
																												 
						""")

banner()

f = open("ips.txt", "r")
targets = f.readlines()
f.close()
if len(targets) < 1:
	print("Please write at least one ip in ips.txt!")
	input("PRESS ANY KEY TO FINISH")
	sys.exit()

tstart = datetime.now()

for ip in targets:
	Portscanner = pslib.Portscanner(ip)
	Portscanner.launch()



tend = datetime.now()
diff = tend - tstart
print("Scan completed in " + str(diff))
datei = open("ports.txt","r")
oports = datei.read()
datei.close()
if oports != "":
	print("Open Ports: ")
	print(oports)
	input("PRESS ENTER TO FINISH")
	sys.exit()
elif oports == "":
	print("No Ports are opened!")
	input("PRESS ENTER TO FINISH")
	sys.exit()
