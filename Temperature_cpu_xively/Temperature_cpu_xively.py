#! /usr/bin/env python
import time
import os
import eeml
import sys
import syslog
import json


def getCPUtemperature():
	res=os.popen('vcgencmd measure_temp').readline()
	return(res.replace("temp=","").replace("'C\n",""))

API_KEY= 'TVzWZitAckDLe0iV7gXeyLLR8w6d9gkkzeULjjotb634AjqB'
FEED =959842380
API_URL ='/v2/feeds/{feednum}.xml' .format(feednum = FEED)

CPU_temp = getCPUtemperature()
print "%s " % CPU_temp
pac = eeml.Pachube(API_URL , API_KEY)

pac.update([eeml.Data("CPU_Temperature", CPU_temp, unit = eeml.Celsius())])

pac.put()
