#!/usr/bin/python3

import requests

from  requests.auth  import  HTTPBasicAuth
#  this is for supplying  http basic authentication 
cred=HTTPBasicAuth('root','cisco')

h={'Accept':'application/json'}
#headers={'Accept':'text/html'}
#  defining  data from that api  in JSON format 
url="http://172.16.6.131/level/15/exec/-/sh/ip/int/br/CR"

#  Now connection  to  restconf -OR -- http protocol 
output=requests.get(url,headers=h,auth=cred)
print(output)
#  only giving  HTTP response code 
print(output.text)
#  giving  HTML based response 
