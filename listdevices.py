import os
import subprocess

def scanDevices():
	os.system("ifconfig -a | sed 's/[ \t].*//;/^$/d' > deviceList")

	f = open("deviceList", "r")

	devices = ""
	for line in f:
		if ":" in line:
			devices += line.replace(":","")
		else:
			devices += line

	g = open ("dev2", "w")
	g.write(devices)

scanDevices()