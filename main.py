import serial.tools.list_ports
from selenium import webdriver
import random
import time
ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()

portsList = []

for onePort in ports:
    portsList.append(str(onePort))
    print(str(onePort))

val = input("Select Port: COM")

for x in range(0,len(portsList)):
    if portsList[x].startswith("COM" + str(val)):
        portVar = "COM" + str(val)
        print(portVar)

serialInst.baudrate = 9600
serialInst.port = portVar
serialInst.open()
driver = webdriver.Chrome()
while True:
    if serialInst.in_waiting:
        time.sleep(2)
        packet = serialInst.readline()
        latAndLong = packet.decode('utf').rstrip('\n').split(",")
        lat = float(latAndLong[0])
        longDirty = latAndLong[1]
        long = float(longDirty[:len(longDirty)-1])
        apiKey = "ddb09aa70dcd4bd2a618401b05008628"
        link = f"https://maps.geoapify.com/v1/staticmap?style=osm-carto&width=600&height=400&center=lonlat:{long},{lat}&zoom=17&apiKey={apiKey}&marker=lonlat:{long},{lat};color:%23ff0000;size:small"
        print(lat,long)
        driver.get(link)