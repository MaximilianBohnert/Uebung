#!/bin/bash
while true

do

	temp=`vcgencmd measure_temp |sed 's/.*=\([0-9]*\)\.\([0-9]*\).*/\1.\2/'`
	echo $temp
	sudo rrdupdate /var/www/html/CPU_Temperatur.rrd N:$temp
	sleep 5
done
