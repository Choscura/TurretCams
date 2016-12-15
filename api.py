"""	

	fast prototype API to allow basic motor function web hooks and motor feedback. For brevity, this is a single file prototype, intended to be expanded into a proper python import and executable program to test things via LAMP and Django over LAN, with the intention of implementing in production VPN networks with full security protocols needed to meet basic security best practices.


Basic structure: 

Initialization: making the turret ready to use. This is an an in-house operation and also a set of self-correcting behaviors.

Motor controls:  This includes two major subsets (at least initially): a manual control mode, where the turret can be aimed by hand, and an automated mode, where the turret can perform specific tasks, such as search patterning, motion tracking, or cycling through a series of known coordinates to take a sequence of motions [aiming a series of photographs or positioning sensors for a sequence of automated measurements et al]

Feedback handling and data passing: This set of functionality includes showing specific sets of relevant data, for example, checking for torque to avoid obstructions to the motor's path of travel.
"""
import logging
logging.basicConfig(level=logging.DEBUG)

import os
import time
import json
from string import *
from threading import Thread



"""try:		#Python 2.7 remaindered versions
	from dxl import *
	from dxl.dxlcore import * 
	from serial import SerialException
except:		#Python 3.5"""

from pyax12.connection import Connection

conn = Connection(port='/dev/ttyACM0', baudrate=100000, timeout=0.1, waiting_time=0.02)
"""
INITIALIZATION

	This is an internal process for the Pi controling the motors to run locally and report on: it should take no variables to run any of this by default, and it should allow the pi to initialize itself independently in any environment it has sufficient power to run in.

This initialization is broken into several parts: for the current iteration, the focus is on building a map of the available points of movement. At a future point, the priority will be to correlate a set of known points with a set of expected visual fedbacks (because, theoretically, a solidly mounted camera turret should see more or less the same things from the same camera positions most of the time, within the confines of environmental variables).

"""

###### Temp section for learning funcitons #######

print("attempting to connect to and scan motors")
ids_available = conn.scan()
print("the scan finished, now it should print something")
for ids in ids_available:
	print("there should be a motor ID here")
	print(ids)
	print (conn.ping(1))


print (conn.ping(0))
print (conn.ping(1))
print (conn.ping(2))
print (conn.ping(3))

def movemotor(motor, point):
	conn.goto(motor, point, speed=0, degrees=False)

def movezero():
	"""
	This is a function to move the motors both to the 512 <centerline> position.
	"""
	conn.goto(1, 512, speed=0, degrees=False)
	conn.goto(2, 512, speed=0, degrees=False)	
	conn.goto(1, 520, speed=0, degrees=False)
	conn.goto(1, 510, speed=0, degrees=False)
	conn.goto(2, 520, speed=0, degrees=False)
	conn.goto(2, 510, speed=0, degrees=False)
	conn.goto(1, 512, speed=0, degrees=False)
	conn.goto(2, 512, speed=0, degrees=False)	

def setup():
	pass
	#move both motors to 512 positon (0^ center for both motors)




"""

"""


"""
MAPPING
"""


"""
MOTORCONTROL
"""

"""
DATAFEED
"""


"""
MAINLOOP
"""
movemotor(1,550)
movemotor(2,550)
movezero()

########################################################################################################
##########		code graveyard, for remaindered and old code that is still nonetheless instructive #####
