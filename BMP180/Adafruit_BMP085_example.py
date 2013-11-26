#!/usr/bin/python

import time
from Adafruit_BMP085 import BMP085

# ===========================================================================
# Example Code
# ===========================================================================

# Initialise the BMP085 and use STANDARD mode (default value)
# bmp = BMP085(0x77, debug=True)
bmp = BMP085(0x77)
fmt = '%m/%d/%Y %H:%M:%S'
# To specify a different operating mode, uncomment one of the following:
# bmp = BMP085(0x77, 0)  # ULTRALOWPOWER Mode
# bmp = BMP085(0x77, 1)  # STANDARD Mode
# bmp = BMP085(0x77, 2)  # HIRES Mode
# bmp = BMP085(0x77, 3)  # ULTRAHIRES Mode
while 1:
	f=open('/home/pi/box/BMP085/sensorsData.html','w')
	time.sleep(30)

	temp = bmp.readTemperature()

# Read the current barometric pressure level
	pressure = bmp.readPressure()

# To calculate altitude based on an estimated mean sea level pressure
# (1013.25 hPa) call the function as follows, but this won't be very accurate
	altitude = bmp.readAltitude()

# To specify a more accurate altitude, enter the correct mean sea level
# pressure level.  For example, if the current pressure level is 1023.50 hPa
# enter 102350 since we include two decimal places in the integer value
# altitude = bmp.readAltitude(102350)
	t = time.strftime(fmt)
	print "Time: %s" % t
	print "Temperature: %.2f C" % temp
	print "Pressure:    %.2f kPa" % (pressure / 1000.0)
	print "Altitude:    %.2f m" % altitude
	print
	f.write("Time: %s " %t)
	f.write("Temperature: %.2f C " % temp)
        f.write("Pressure:    %.2f kPa " % (pressure /1000.0))
        f.write("Altitude:    %.2f m" % altitude)
        f.close()
        time.sleep(30)
