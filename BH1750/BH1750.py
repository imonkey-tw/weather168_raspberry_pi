import smbus
import time

BH1750Address = 0x23
bus = smbus.SMBus(1)

def getIlluminace():

    	result=bus.read_i2c_block_data(BH1750Address,0x11) #1lx reolution 120ms
	time.sleep(0.5)
	return int((result[1])+(256*result[0])/1.2)


print "I=",getIlluminace()
