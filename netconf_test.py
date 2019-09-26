#!/usr/bin/python3
import  time
from  ncclient  import  manager
#  this code will act as  netconf client 

#  using  connect function with manager to connect   NetCONF enabled device
device=manager.connect(host='172.16.6.131',username='root',password='cisco',port=22,allow_agent=False,look_for_keys=False,hostkey_verify=False)
print(device)
print("______________________________")
print("______________________________")
time.sleep(2)
print(dir(device))
print("@@@@@@@@@@@@@@@@@@@@@")
time.sleep(1)
print(device.get_config('running').data_xml)
