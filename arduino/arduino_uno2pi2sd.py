#!/usr/bin/python

import serial
import time
fmt = '%m/%d/%Y %H:%M:%S'
ser =serial.Serial('/dev/ttyS1',57600)
val = ser.readline()
val = ""
time.sleep(10)
while 1:
	f=open('/home/pi/box/'+time.strftime('%Y%m%d')+'sensorslog.csv','a')
	time.sleep(10)
	val=ser.readline()
	t=time.strftime(fmt)
	f.write("\n{"+"\""+t+"\" : "+val+"}\n")
	print "\n{"+"\""+t+"\" : "+val+"}\n"
	f.close()
        val=""
	time.sleep(10)
        
