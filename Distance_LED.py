#!/usr/bin/python3

import time
import VL53L0X
import spidev


def writeWS2812(spi, color):
        list=[]
        for rgb in color:
                for byte in [rgb[1],rgb[0],rgb[2]]:
                        for ibit in range(7,-1,-1):
                                if(byte>>ibit)&1 == 1:
                                        list.append(0xF8)
                                else:
                                        list.append(0x80)
        spi.xfer(list, int(8/1.25e-6))


# Create a VL53L0X object
tof = VL53L0X.VL53L0X()

# Start ranging
tof.start_ranging(VL53L0X.VL53L0X_BETTER_ACCURACY_MODE)

timing = tof.get_timing()
if (timing < 20000):
    timing = 20000
print ("Timing %d ms" % (timing/1000))

while (1):
    distance = tof.get_distance()
    if (distance > 0):
        print ("%d mm, %d cm" % (distance, (distance/10)))

    spi = spidev.SpiDev()
    spi.open(0,0)

    if (distance < 150):
        writeWS2812(spi, [[10,0,0]]*5)
    if (distance < 300):
        writeWS2812(spi, [[25,25,0]]*5)
    else:
        writeWS2812(spi, [[0,10,0]]*5)


    time.sleep(0.2)

tof.stop_ranging()

#spi = spidev.SpiDev()
#spi.open(0,0)
#if (distance < 100):
#	writeWS2812(spi, [[10,0,0]]*5)
#if (distance < 250):
#	writeWS2812(spi, [[10,10,0]]*5)
#else:
#	writeWS2812(spi, [[0,0,10]]*5)
