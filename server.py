#receiver

import os
from socket import *
cmd=' echo $(seq 254) | xargs -P255 -I% -d" " ping -W 1 -c 1 192.168.43.% | grep -E -o "[0-1].*?:" > ip.txt'
os.system(cmd)

cmd2="ip route get 8.8.4.4 | head -1 | awk '{print $7}' > ip_own.txt"
os.system(cmd2)

# f_ip=open("ip_own.txt","r")

# ip_own=f_ip.readline()

# #print ip_own


# f=open("ip.txt","r")

# ip1=f.readline()
# ip2=f.readline()
# ip3=f.readline()
# ip4=f.readline()

# ip1=ip1[:-2]
# ip2=ip2[:-2]
# ip3=ip3[:-2]
# #ip4=ip4[:-2]

# print ip1
# print ip2
# print ip3
# #print ip4

# if ((ip1=="192.168.1.1" or ip1==ip_own) and (ip2==ip_own or ip1="192.168.1.1")):
#     host=ip3
# else if ((ip2==ip_own or ip2=="192.168.1.1") and (ip3=="192.168.1.1" or ip3==ip_own)):
#     host=ip1
# else if ((ip3==ip_own or ip3=="192.168.1.1") and (ip1=="192.168.1.1" or ip1==ip_own)):
#     host=ip2

#host = ""
#port = 13000
#buf = 1024
#addr = (host, port)
#UDPSock = socket(AF_INET, SOCK_DGRAM)
#UDPSock.bind(addr)
#print "Waiting to receive messages..."
#while True:
#    (data, addr) = UDPSock.recvfrom(buf)
#    print "Received message: " + data
#    if data == "exit":
#        break
#UDPSock.close()
#os._exit(0)


send_cmd="nc -lp 4000 > received_file"
os.system(send_cmd)
