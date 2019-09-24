#!/usr/bin/python3

import  paramiko,time,sys

# using  as  ssh client  
client=paramiko.SSHClient()
#  auto adjust  host key verification  with yes or no 
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#  create  list  of  devices  
device_ip=["172.16.6.131","172.16.6.131","172.16.6.131"]
u='root'
p='cisco'
#  apply for loop 
for  i  in  device_ip : 
	print("Connectng  with  device  :  ",i)
	client.connect(i,username=u,password=p,allow_agent=False, look_for_keys=False)
	device_access=client.invoke_shell()
	device_access.send("term len 0\n")
	device_access.send("sh run \n")
	time.sleep(1)
	output=device_access.recv(65000)
	print(output.decode('ascii'))
	print("_______________________")
	print("_______________________")
	#  storing  file
	with open(i+time.ctime(),'w') as  f:
		f.write(output.decode('ascii'))
		time.sleep(1)










