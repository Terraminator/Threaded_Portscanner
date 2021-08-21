import socket
import sys
import threading
from time import sleep
from datetime import datetime
import os

content = ""
path = os.getcwd() + "\\ips.txt"
if not os.path.exists(path):
	with open("ips.txt", "w") as f:
		f.write("")
f = open("ips.txt", "r")
targets = f.readlines()
f.close()
if len(targets) < 1:
	print("Please write at least one ip in ips.txt!")
	input("PRESS ANY KEY TO FINISH")
	sys.exit()

with open("ports.txt", "w") as f:
	f.write("")
tstart = datetime.now()

def scanner(y):
	content = ""
	id = threading.currentThread().getName()
	p = y[0]
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	res = sock.connect_ex((targetIP, p))
	if res == 0:
		print("Open Connection in Port: " + str(p))
		datei = open("ports.txt","a+")
		datei.write(str(p) + ", ")
		datei.close()
	sock.close()

for ip in targets:
	with open("ports.txt", "a+") as f:
		f.write("\n")
		f.write(ip)
		f.write("\n")
	q = 1
	if "www" in ip or "org" in ip or "com" in ip or "de" in ip or "en" in ip or "us" in ip or "ch" in ip:
		ip = socket.gethostbyname(ip)
	targetIP = ip
	print(ip + "\n")
	while q < 4501:
		try:
			x = [q]
			t = threading.Thread(target=scanner, args=[x])
			t.start()
			q = q + 1
		except:
			sleep(0.5)
			q = q - 1
	

tend = datetime.now()
diff = tend - tstart
print("Scan completed in " + str(diff))
datei = open("ports.txt","r")
oports = datei.read()
datei.close()
if oports != "":
	print("Open Ports: ")
	print(oports)
	input("PRESS ANY KEY TO FINISH")
	sys.exit()
elif oports == "":
	print("No Ports are opened!")
	input("PRESS ANY KEY TO FINISH")
	sys.exit()
