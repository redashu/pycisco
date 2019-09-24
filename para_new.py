#!/usr/bin/python3

import  paramiko,time,sys

# using  as  ssh client  
client=paramiko.SSHClient()
#  auto adjust  host key verification  with yes or no 
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#  time for connecting to remote Cisco IOS
addr=sys.argv[1]   #  first  argument as  IP 
u=sys.argv[2]  #   username as  second  argument
p=sys.argv[3]  #   password is  third  argument 
#  connected with ssh session 
client.connect(addr,username=u,password=p,allow_agent=False, look_for_keys=False)
#  we have to ask for shell 
device_access=client.invoke_shell()
#  now sending  command
device_access.send("term len 0\n")
device_access.send("sh run \n")
time.sleep(1)
#  assume command got executed so lets recv data 
output=device_access.recv(65000)
print(type(output))
#   decoding  byte - like  string  into  string 
print(output.decode('ascii'))
#  now  want to save  output in a file 
with open("csr1000v_1.txt",'w')  as  f:
	f.write(output.decode('ascii')) 







