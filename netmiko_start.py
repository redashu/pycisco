from netmiko import ConnectHandler

cisco_csr = {
    'device_type': 'cisco_ios'    ,
    'host':   '172.16.6.131'   ,
    'username': 'root',
    'password': 'cisco',
    'port' : 22          # optional, defaults to 
}

#  connectionhandler  is  supporting  dictonary format 
