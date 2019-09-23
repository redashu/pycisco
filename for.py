#!/usr/bin/python3

'''
x=input("type number :  ")
print(x)
'''
from  time import  sleep
import  sys
data=sys.argv[1:]

sum=0
for  i  in    data  :
	sum=sum+int(i)

print(sum)



