"""
	python 2 test code for dynamixel ax12a turretcam
"""

import random

from dxl.dxlchain import DxlChain

# Open the serial device
chain=DxlChain("/dev/ttyACM0",rate=1000000)

# Load all the motors and obtain the list of IDs
motors=chain.get_motor_list() # Discover all motors on the chain and return their IDs
print motors

#center motors for mounting orientation
chain.sync_write_pos([1,2], [512,512])

# this corresponds to the position limits of a current <as of this writing> turret prototype. No automatic handling yet.
xmin = 0		# 	theoretical min 0
xmax = 1023		#	theoretical max 1023
ymin = 150		
ymax = 550		

x_position_variable = 512
y_position_variable = 512

def curses():
	# import curses
	import curses
	# Get the curses window, turn off echoing of keyboard to screen, turn on
	# instant (no waiting) key response, and use special values for cursor keys
	screen = curses.initscr()
	curses.noecho() 
	curses.cbreak()
	screen.keypad(True)
	try:		#the premise of this is to give a variable that can be modified to move the motors around
		while True: 
			chain.goto(1, x_position_variable)	
			chain.goto(2, y_position_variable)
			char = screen.getch()
			if char == ord('q'):
				break
			elif char == curses.KEY_UP:
				print "up"
				if (y_position_variable +1) <= ymax:
					y_positon_variable = y_position_variable + 1 
				else:
					print "no!"
			elif char == curses.KEY_DOWN:
				print "down"
			elif char == curses.KEY_RIGHT:
				print "right"
				Connection.goto(1, 0, speed=100, degrees=False)
			elif char == curses.KEY_LEFT:
				print "left"
				Connection.goto(1, 1023, speed=100, degrees=False)
			elif char == 10:
				print "stop"   

	finally:
		#Close down curses properly, inc turn echo back on!
		curses.nocbreak(); screen.keypad(0); curses.echo()
		curses.endwin()

curses()
"""
# Move a bit
chain.goto(1,500,speed=200) # Motor ID 1 is sent to position 500 with high speed
chain.goto(1,400)                    # Motor ID 1 is sent to position 100 with last speed value

chain.goto(1,0, speed=1023)
chain.goto(1,750, speed=1023)

#	move Y axis motor
chain.goto(2,150, speed=1023)	# straight vertical 
chain.goto(2,550)				# should be lowest available 

#	outofwhacking everything
chain.goto(1,random.randint(0,750),speed=1023)
chain.goto(2,random.randint(150,550)	,speed=1023)

#zero everything back
chain.goto(1,512, speed=144)
chain.goto(2,512, speed=144)
while chain.is_moving():
	print chain.get_reg_si(id, "present_position")

# Move and print current position of all motors while moving
chain.goto(1,400,speed=20,blocking=False) # Motor ID 1 is sent to position 1000
while chain.is_moving():
    print chain.get_position()
"""
# Disable the motors
chain.disable()
