#!/usr/bin/python3
import netmiko 
# multi vendor library 
from  getpass import  getpass 
sec=getpass("plz enter password  for device : ")
# accept password without showing in screen 
device1={
	'username' : 'root',
	'password' : sec,
	'device_type' : 'cisco_ios',
	'host' : '172.16.6.12'
}

sec1=getpass("plz enter password  for device : ")
device2={
	'username' : 'root',
	'password' : sec1,
	'device_type' : 'cisco_ios',
	'host' : '172.16.6.131'
}

device3={
	'username' : 'root',
	'password' : 'cisco',
	'device_type' : 'ciscoii_ios',
	'host' : '172.16.6.132'
}

for  i in  [device1,device2,device3] :
	try : 
		print("connecting  with Device type :--- > ",i['device_type']," Having IP ",i['host'])
		print("________________________________________")
		print("________________________________________")
		print("________________________________________")
		device_connect=netmiko.ConnectHandler(**i)
		# sending command 
		output=device_connect.send_command("show ip int br")
		print(output)
		print("________________________________________")
		print("________________________________________")
		print("________________________________________")
	except netmiko.ssh_exception.NetMikoTimeoutException :
		print("Please check your IP or network thing : ",i['host'])
	except netmiko.ssh_exception.NetMikoAuthenticationException :
		print("Please check your Authentication Details for Device : ",i['host'])
	except  ValueError :
		print("make sure your device category fro host ",i['host'])
