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
	flight_temps_press = open('flight_temps_press', 'r+')###!!! is this proper syntax??? #Open file to be edited
	flight_temps_press.seek(2)#go to end of file
	
	flight_temps_press.write('temp ', temp, ' pressure ', pressure, ' altitude ', altitude, \n) #write out data in a format suitable for .CSV export

	delta_f = time.clock () #end time
	delta = 6 - (delta_f - delta_i) #make sure data readings are taken 6 seconds apart #############Should be using more or less than 6 sec?############
#	Print (delta)
###^^^^^Above used to validate whether it is working or not, uncomment to test^^^^^^###
	time.sleep (delta) #sleep 6 sec
	
###Current code makes it necesary to use a fresh file every time.###
	
