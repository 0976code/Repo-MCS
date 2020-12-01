#!/usr/bin/python3
import RPi.GPIO as GPIO
import time
import requests
import sys
import http.client as http
import urllib
import json

# Set the LED PIN
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
ledPin = 2
GPIO.setup(ledPin,GPIO.OUT)

deviceId = "D91SYUp0"
deviceKey = "Zt8h20yZldy8m8sl"

def get_to_mcs():
	host = "http://api.mediatek.com"
	endpoint = "/mcs/v2/devices/" + deviceId + "/datachannels/LEDControl/datapoints"
	url = host + endpoint
	headers = {"Content-type": "application/json", "deviceKey": deviceKey}
	r = requests.get(url,headers = headers)
	value = (r.json()["dataChannels"][0]["dataPoints"][0]["values"]["value"])
	return value
while(True):
	if(get_to_mcs() == 1):
		print("LED turning on.")
		GPIO.output(ledPin,GPIO.HIGH)
		time.sleep(0.5)
	elif(get_to_mcs() == 0):
		print("LED turning off.")
		GPIO.output(ledPin,GPIO.LOW)
		time.sleep(0.5)
