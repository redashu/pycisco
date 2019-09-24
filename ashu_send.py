#!/usr/bin/python3

import  socket,time
#   checking  for  socket  functions

print([i for  i  in dir(socket) if  'socket' in i])

#  now creating  UDP  socket 
#  ipv4  socket  --  ipv4  + 2 byte port 
#  ipv6  socket   -- ipv6  + 2 byte port 
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  
#                for Ipv4  ,   for  UDP socket 
#socket.socket(socket.AF_INET,socket.SOCK_STREAM) #  for tcp    

while True : 
	msg=input("enter  data  to  send  :  ")
	newmsg=msg.encode('ascii')
	s.sendto(newmsg,("127.0.0.1",8899))
	data=s.recvfrom(10000)
	print(data)




