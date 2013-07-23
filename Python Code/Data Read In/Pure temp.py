###This tempurature sesnsor will be attached directly to the heatsink/processor core.
###The purpose of this is to both a) have a failsafe in case the primary BMP sensor fails
###This code may need a dedicated code base similar to the adafruit base. Should ask Drew about this

import time


temp = #???????????


#This code is used in order to test the sensor, and should be commented out eventually.



print ("Temp= ", temp, ' degC')





#This code is used to actually print to the file.

while(1==1):
    delta_i = time.clock ()

    sole_temp = open('sole_temp', 'r+') ###!?! is this proper syntax????
    sole_temp.seek(2)
    sole_temp.write('Core temp ', temp, \n)

    delta_f = time.clock ()
    delta = 6 - (delta_f - delta_i)
    print (delta)

    time.sleep (delta)

    
