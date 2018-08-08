from tkinter import *
import os
import subprocess
import signal
# Custom Functions
from listdevices import *

global pid
deviceList = ""

def airmon(test):
	with open("deviceList") as file:
		devList = file.readlines()
		devList = [devList.strip() for word in file]
	scanDevices()

	g = open ("dev2", "r")
	for line in g:
		print(line)
	com = input("What is your wireless interface? ")
	subprocess.Popen(["sudo", "airmon-ng", "start", test])

def adapter():
	os.system("ip link > adapter.txt")
	f = open("adapter.txt","r")
	for line in f:
		if line.find("wls1"):
			com = "wls1"
			return com
			break
		elif line.find("wlan0"):
			com = "wlan0"
			return com
			break

def stopMon():
	mon = input("Which monitor whould you like to stop? ")
	subprocess.Popen(["sudo", "airmon-ng", "stop", mon])

def startDump():
	choice = input("Do you want to start or stop? ")
	os.system("gnome-terminal")
	os.system("sudo airodump-ng -c 1,6,11 -w test mon0")
	f = open("DumpProcess.txt", "w")
	p = subprocess.Popen(["sudo", "airodump-ng", "-c 1,6,11", "-w test", "mon0"])
	pid = p.pid
	a = str(p.pid)
	f.write(a)
	return p

def startMDK():
	q = subprocess.Popen(["sudo", "mdk3", "mon0", "d", "-c 1,6,11"])
	return q

def stopDump():
	os.system("sudo pkill -f airodump")
	f = open("DumpProcess.txt", "r")
	for	line in f:
		a = int(line)
		os.kill(pid, signal.SIGKILL)
		break
def stopMDK():
	os.system("sudo pkill -f mdk3")

# Writes network device names to file
scanDevices()

class App:

	

	def __init__(self,master):

		frame = Frame(master)
		frame.pack()
		frame2 = Frame(master)
		frame2.pack()

		# **** Toolbar ****
		menu = Menu(master)
		master.config(menu=menu)

		# File Menu
		fileMenu = Menu(menu)
		menu.add_cascade(label="File", menu=fileMenu)
		fileMenu.add_command(label="Quit", command=exit) ###### Change Command

		# Monitor Menu and submenus
		monMenu = Menu(menu)
		airmonMenu = Menu(menu)
		airmonSelect = Menu(menu)

		menu.add_cascade(label="Monitor", menu=monMenu)
		monMenu.add_cascade(label="Airmon", menu=airmonMenu)


		# Airmon Submenu
		airmonMenu.add_cascade(label="Start Monitor", menu=airmonSelect)
		airmonMenu.add_command(label="Stop Monitor", command=stopMon)

		g = open("dev2", "r")
		for line in g:
			airmonSelect.add_command(label=line, command=lambda: airmon(line))


		self.detAdapter = Button(frame, text="Determine Wireless Adapter", command=adapter)
		self.detAdapter.pack(side=LEFT)

		#self.sudo = Button(frame, text="Load Sudo", command=sudo)
		#self.sudo.pack(side=LEFT)


		self.button = Button(frame, text="Start airmon-ng", command=airmon)
		#self.button.grid(row=0, column=0)

		self.stopAir = Button(frame, text="Stop airmon-ng", fg="red", command=stopMon)
		#self.stopAir.grid(row=1, column=0)

		self.startDump = Button(frame, text="Start airodump-ng", command=startDump)
		self.startDump.pack(side=LEFT)

		self.stopDump = Button(frame2, text="Stop airodump-ng", fg="red", command=stopDump)
		self.stopDump.pack(side=LEFT)

		self.startMDK = Button(frame, text="Start MDK3", command=startMDK)
		self.startMDK.pack(side=LEFT)

		self.stopMDK = Button(frame2, text="Stop MDK3", fg="red", command=stopMDK)
		self.stopMDK.pack(side=LEFT)

		self.quit = Button(frame2, text="Quit", command=frame.quit)
		self.quit.pack()

root = Tk()
mon = 0
app = App(root)



root.mainloop()