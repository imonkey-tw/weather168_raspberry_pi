import smbus
import time
import xively
import datetime

BH1750Address = 0x23
bus = smbus.SMBus(1)

API_KEY ='TVzWZitAckDLe0iV7gXeyLLR8w6d9gkkzeULjjotb634AjqB'
FEED_ID = 959842380
api = xively.XivelyAPIClient(API_KEY)
feed = api.feeds.get(FEED_ID)

def getIlluminace():

    	result=bus.read_i2c_block_data(BH1750Address,0x11) #1lx reolution 120ms
	time.sleep(0.5)
	return int((result[1])+(256*result[0])/1.2)


Illuminace_BH1750=getIlluminace()
print "I=",Illuminace_BH1750

try:
	datastream = feed.datastreams.get("Illuminace_BH1750")
except:
	datastream = feed.datastreams.create("Illuminace_BH1750")

datastream.current_value = Illuminace_BH1750
datastream.at = datetime.datetime.utcnow()
datastream.update()
