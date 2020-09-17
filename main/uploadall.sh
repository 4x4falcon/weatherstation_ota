#! /bin/bash

echo "Reseting..."
ampy -p $1 -b 115200 reset
sleep 2
ampy -p $1 -b 115200 ls
echo "uploading boot.py..."
ampy -p $1 -b 115200 put boot.py
sleep 2

echo "uploading ws..."
ampy -p $1 -b 115200 mkdir ws
sleep 2

echo "uploading ws/main..."
ampy -p $1 -b 115200 mkdir ws/main
sleep 2

echo "uploading ws/main/classes..."
ampy -p $1 -b 115200 mkdir ws/main/classes
sleep 2


#echo "uploading ws/main/ws.py..."
#ampy -p $1 -b 115200 put ws/main/ws.py ws/main.ws.py

#echo "uploading bme280.py..."
#ampy -p $1 -b 115200 put classes/bme280.py classes/bme280.py
#sleep 2
#echo "uploading debounce.py..."
#ampy -p $1 -b 115200 put classes/debounce.py classes/debounce.py
#sleep 2

#echo "uploading lib..."
#ampy -p $1 -b 115200 mkdir lib
#sleep 2
#ampy -p $1 -b 115200 put lib/urequests.py lib/urequests.py
#sleep 2
#ampy -p $1 -b 115200 put lib/ssd1306.py lib/ssd1306.py
#sleep 2
#echo "uploading functions.py..."
#ampy -p $1 -b 115200 put functions.py
#sleep 2

#echo "uploading main.py..."
#ampy -p $1 -b 115200 put main.py
#sleep 2

echo

ampy -p $1 -b 115200 ls
sleep 2
ampy -p $1 -b 115200 ls ws

