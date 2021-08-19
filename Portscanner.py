import socket
import sys
import threading
from time import sleep
from datetime import datetime


content = ""
target = "46.223.131.234"
#targetIP = socket.gethostbyname(target)
targetIP = target

tstart = datetime.now()
def scanner(y):
	content = ""
	id = threading.currentThread().getName()
	p = y[0]
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	res = sock.connect_ex((targetIP, p))
	if res == 0:
		print("Offene Verbindung in Port " + str(p))
		datei = open("ports.txt","a+")
		datei.write(str(p) + ", ")
		datei.close()
	sock.close()


q = 1
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
print("Die Ports " + oports + "sind offen")
datei.close()
