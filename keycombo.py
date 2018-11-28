import os
import sys
from socket import *
from pynput import keyboard


# The key combination to check
COMBINATIONS = [
    {keyboard.Key.ctrl, keyboard.KeyCode(char='c')}
]

COMBINATION = [
    {keyboard.Key.ctrl, keyboard.KeyCode(char='q')}
]

# The currently active modifiers
current = set()

def execute_send():
	print ("Sending")
	cmd="nmap -sP 192.168.43.* | grep -o 192.* | tr -d '()' > ip.txt"
	os.system(cmd)

	cmd2="ip route get 8.8.4.4 | head -1 | awk '{print $7}' > ip_own.txt"
	os.system(cmd2)

	f_ip=open("ip_own.txt","r")

	ip_own=(f_ip.readline()).rstrip('\n')

	#print ip_own


	f=open("ip.txt","r")

	ip1=(f.readline()).rstrip('\n')
	ip2=(f.readline()).rstrip('\n')
	ip3=(f.readline()).rstrip('\n')

	#print ip1
	#print ip2
	#print ip3
	#print ip4
	host=''

	lis=[]
	ip_own.rstrip('\n')
	lis.append("192.168.43.1")
	lis.append(ip_own)

	ips=[ip1,ip2,ip3]
	# print ips
	# print lis
	for ip in ips:
	    if(ip not in lis):
		host = ip
		host.rstrip('\n')
		break;

	# print host

	#if ((ip1=="192.168.43.1" or ip1==ip_own) and (ip2==ip_own or ip2=="192.168.43.1")):
	#    host=ip3
	#elif ((ip2==ip_own or ip2=="192.168.43.1") and (ip3=="192.168.43.1" or ip3==ip_own)):#
	#    host=ip1
	#elif ((ip3==ip_own or ip3=="192.168.43.1") and (ip1=="192.168.43.1" or ip1==ip_own)):
	#    host=ip2

	#print host
	#host =""
	# set to IP address of target computer
	#port = 13000
	#addr = (host, port)
	#UDPSock = socket(AF_INET, SOCK_DGRAM)
	#while True:
	#    data = raw_input("Enter message to send or type 'exit': ")
	#    UDPSock.sendto(data, addr)
	#    if data == "exit":
	#        break
	#UDPSock.close()
	#os._exit(0)

	os.system("xclip -o > copy.txt")
	f3=open("copy.txt","r")
	text=(f3.readline()).rstrip('\n')

	#print text

	send_cmd="echo "+text+" | nc "+host+" 4000"
	#print send_cmd
	os.system(send_cmd)
	

def execute_receive():
    print ("Receiving")

def on_press(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS):
            execute_send()

    if any([key in COMBO for COMBO in COMBINATION]):
        current.add(key)
        if any(all(k in current for k in COMBO2) for COMBO2 in COMBINATION):
            execute_receive()

def on_release(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.remove(key)
    

    

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
