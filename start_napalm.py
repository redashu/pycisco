#!/usr/bin/python3

from  napalm  import  get_network_driver
driver=get_network_driver('ios')
#  connecting to device
device=driver('172.16.6.131','root','cisco')
print([i for i in  dir(device) if 'load' in i])
#  open sessoin with device 
device.open()
#merging  configuration
#  only copy config file to router using scp   
device.load_merge_candidate(filename='myrouter.txt')

#  check the diff 
print(device.compare_config())

#  now to commit the applied configuration 

c=input("confirm with y|n to apply configuration : ")

if  c == 'y' or  c  == 'Y'  :

	print("Commiting  the configuration ")
	device.commit_config()
	res=input("do you want to rollback changes : y|n")
		if  res == 'y' or res == 'Y' :
			device.rollback()
		else :
			print("No rollbacks applied ")
elif  c == 'n'  or  c == 'N' :
	print("discarding configuration ")
	device.discard_config()
else :
	print("please type only  y|Y  or  n\N")
	

#  close connection as well
device.close()

