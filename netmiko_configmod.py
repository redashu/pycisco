#!/usr/bin/python3

import netmiko 
# multi vendor library 

device1={
	'username' : 'root',
	'password' : 'cisco',
	'device_type' : 'cisco_ios',
	'host' : '172.16.6.131'
}
#  to connect target device 
#  by checking  couple of things connecthandler will allow you to connect
'''
	.  device_type 

'''
device_connect=netmiko.ConnectHandler(**device1)
print([i for i  in  dir(device_connect) if 'send' in i])
#  now sending configuration for devices
conf=["hostname  pyrouter1","username hello privi 10 password  cisco"]
output=device_connect.send_config_set(conf)
print(output)
#   sending  configuration from file
output1=device_connect.send_config_from_file('myrouter.txt')
print(output1)




