"""
AM2301.py
Temperature/Humidity monitor using Raspberry Pi and AM2301(DHT21).
Data is displayed at thingspeak.com
Original author: Mahesh Venkitachalam at electronut.in
Modified by Funputer on April 19, 2018
"""
import sys
import RPi.GPIO as GPIO
from time import sleep
import Adafruit_DHT
import urllib2
myAPI = "GEKV7NZ2FBGZRUZL"
def getSensorData():
   RH, T = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, 4)
   return (str(RH), str(T))
def main():
   print 'starting...'
   baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI
   while True:
       try:
           RH, T = getSensorData()
           f = urllib2.urlopen(baseURL +
                               "&field1=%s&field2=%s" % (RH, T))
           print RH, T, f.read()
           f.close()
           sleep(30) #uploads AM2301 sensor values every 30 seconds.
       except:
           print 'exiting.'
           break
# call main
if __name__ == '__main__':
   main()
