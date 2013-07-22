### This code controls the writing to the output file named 'flight_temps_press'
### Coment out code blocks as necesaary for testing etc. 
### the initial code is designed to print to the output
#######################################################################
####### this code can only exist using the adafruit code base #########
#######################################################################
import time

from Adafruit_BMP085 import BMP085

bmp = BMP085(0x77)

temp = bmp.readTempurature()
pressure = bmp.readPressure()
altitude = bmp.readAltitude()

print ("Temp = %.2f C") % temp
print ("Pressure = %.2f hPa") % (pressure/100)
print ("altitude = %.2f ") % altitude



#####################################################################
###### This code is used for actually writing to files ##############
#####################################################################

while(1==1):
        delta_i = time.clock () ###!!! should we be using time.CLOCK_REALTIME ??? !!!###
	flight_temps_press = open('flight_temps_press', 'r+')
	flight_temps_press.seek(2)
	
	flight_temps_press.write('temp' temp, 'pressure' pressure, 'altitude' altitude)

	delta_f = time.clock ()
	delta = 6 - (delta_f - delta_i)
#	Print (delta)
###^^^^^Above used to validate whether it is working or not, uncomment to test^^^^^^###
	time.sleep (delta)
	
