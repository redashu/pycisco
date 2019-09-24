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

###  for  receiver  only  
s.bind(("",8899)) 
#  8891 -- 8899
#   bind  will accept  tuple format  ip & port  
while True : 
	data=s.recvfrom(1000) #  this buffer size 
	print(data[0])
	print("sender address is  ",data[1]) 
	msg=input("enter  rply  :  ")
	newmsg=msg.encode('ascii')
	s.sendto(newmsg,data[1])

s.close()
