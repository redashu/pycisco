#!/usr/bin/python3

import netmiko,time 
# multi vendor library 

device1={
	'username' : 'root',
	'password' : 'cisco',
	'device_type' : 'cisco_ios',
	'host' : '172.16.6.131'
}

device_connect=netmiko.ConnectHandler(**device1)
output=device_connect.send_command("show ip int br")
output1=device_connect.send_command("show ip int br",use_textfsm=True)
print(output)
#print(output1)
for  i  in  output1:
	print("my Interface name is  ",i['intf']," with IP ",i['ipaddr']," having status ",i['status'])
	time.sleep(1)
