import socket
import sys
import threading
from time import sleep
from datetime import datetime
import os


class Portscanner:
	def __init__(self, ip):
		self.ip = ip
		path = os.getcwd() + "\\ips.txt"
		with open("ports.txt", "w") as f:
			f.write("")
			
		if not os.path.exists(path):
			with open("ips.txt", "w") as f:
				f.write("")


	def scanner(self, y):
		try:
			p = y[0]
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			res = sock.connect_ex((str(self.targetIP), p))
			if res == 0:
				print("Open Connection in Port: " + str(p))
				datei = open("ports.txt","a+")
				datei.write(str(p) + ", ")
				datei.close()
			sock.close()
		except:
			pass

	def launch(self):
		if self.ip != "":
			with open("ports.txt", "a+") as f:
				f.write("\n")
				f.write(self.ip)
				f.write("\n")
			q = 1
			if "www" in self.ip or "org" in self.ip or "com" in self.ip or "de" in self.ip or "en" in self.ip or "us" in self.ip or "ch" in self.ip:
				self.ip = socket.gethostbyname(ip)
			self.targetIP = self.ip.replace("\n", "")
			print(self.ip + "\n")
			while q < 4501:
				try:
					x = [q]
					t = threading.Thread(target=self.scanner, args=[x])
					t.start()
					q = q + 1
				except:
					sleep(0.5)
					q = q - 1

