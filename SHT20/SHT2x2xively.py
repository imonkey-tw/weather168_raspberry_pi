#!/usr/bin/python
import xively
import datetime
import smbus
import time



API_KEY ='TVzWZitAckDLe0iV7gXeyLLR8w6d9gkkzeULjjotb634AjqB'
FEED_ID = 959842380
api = xively.XivelyAPIClient(API_KEY)
feed = api.feeds.get(FEED_ID)

#**********************************************************SHT20

eSHT2xAddress       = 0x40
eTempHoldCmd	    = 0xE3
eRHumidityHoldCmd   = 0xE5
eTempNoHoldCmd      = 0xF3
eRHumidityNoHoldCmd = 0xF5
writeUserRegister   = 0xE6
readUserRegister    = 0xE7
softReset           = 0xFE 
bus = smbus.SMBus(1)

#******************************************************************************
#* Global Functions
#******************************************************************************/

#**********************************************************
#* GetHumidity
#*  Gets the current humidity from the sensor.
#*
#* @return float - The relative humidity in %RH
#**********************************************************/
def getRHumidity():
	
		return (-6.0 + 125.0 / 65536.0 * float(readSensor(eRHumidityNoHoldCmd)))
		
	


#***************************************************************/
#* GetTemperature
#*  Gets the current temperature from the sensor.
#*
#* @return float - The temperature in Deg C
#**********************************************************/
def getTemperature():
	
		return (-46.85 + 175.72 / 65536.0 * float(readSensor(eTempNoHoldCmd)))
	


#******************************************************************************/
#* Private Functions
#******************************************************************************/

def readSensor(command):	
		bus.write_quick(eSHT2xAddress)
		bus.write_byte(eSHT2xAddress,command)
		time.sleep(0.1)
		result =(bus.read_byte(eSHT2xAddress)<<8)
		result += bus.read_byte(eSHT2xAddress)
		result &= ~0x0003   # clear two low bits (status bits)(0x0003=00000000 00000011 =>~0x0003=11111111 11111100=> &=xxxxxxxx xxxxxx00)
		return result
	
Temperature_SHT20=round(getTemperature(),2)
RHumidity_SHT20=int(getRHumidity())
print "H=",RHumidity_SHT20
print "T=",Temperature_SHT20


#******************************************************************************/
 

 

try:
	datastream = feed.datastreams.get("Temperature_SHT20")
except:
	datastream = feed.datastreams.create("Temperature_SHT20")

datastream.current_value = Temperature_SHT20
datastream.at = datetime.datetime.utcnow()
datastream.update()



try:
	datastream = feed.datastreams.get("RHumidity_SHT20")
except:
	datstream = feed.datastreams.create("RHumidity_SHT20")

datastream.current_value = RHumidity_SHT20
datastream.at = datetime.datetime.utcnow()
datastream.update()
