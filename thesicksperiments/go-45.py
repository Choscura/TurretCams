from pyax12.connection import Connection

# Connect to the serial port
serial_connection = Connection(port="/dev/ttyACM0", baudrate=100000)

print("scanning")
# Ping the dynamixel unit(s)
ids_available = serial_connection.scan()




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
		#x_position_variable = 512
		#y_position_variable = 512
		while True: 
			#posx = int(serial_connection.get_present_position(1, degrees=False))
			#posy = int(serial_connection.get_present_position(2, degrees=False))
			char = screen.getch()
			if char == ord('q'):
				break
			elif char == curses.KEY_UP:
				print("Fuck!")
				#posy = posy + 1
				Connection.goto(Connection, dynamixel_id=1, position=512, speed=512, degrees=False)
				Connection.goto(Connection, dynamixel_id=2, position=700, speed=512, degrees=False)
			elif char == curses.KEY_DOWN:
				Connection.goto(1, position=512, speed=512, degrees=False)
				Connection.goto(2, position=512, speed=512, degrees=False)
				print("down")
			elif char == curses.KEY_RIGHT:
				print("right")
				Connection.goto(1, 0, speed=100, degrees=False)
			elif char == curses.KEY_LEFT:
				print("left")
				Connection.goto(1, 1023, speed=100, degrees=False)
			elif char == 10:
				print("stop")   

	finally:
		#Close down curses properly, inc turn echo back on!
		curses.nocbreak(); screen.keypad(0); curses.echo()
		curses.endwin()

"""
print("Scanned")
for dynamixel_id in ids_available:
	print(dynamixel_id)
	serial_connection.goto(dynamixel_id, 512, speed=512, degrees=False)	
	print ("something should've moved")
	serial_connection.goto(dynamixel_id, 524, speed=512, degrees=False)
	serial_connection.goto(dynamixel_id, 500, speed=512, degrees=False)
	serial_connection.goto(dynamixel_id, 512, speed=512, degrees=False)
	

curses()
      #while True:
# Go to -45° (45° CW)
#serial_connection.goto(dynamixel_id, -45, speed=512, degrees=True)
#time.sleep(1)    # Wait 1 second
#serial_connection.goto(dynamixel_id, 45, speed=512, degrees=True)
#time.sleep(1)
# Close the serial connection
#serial_connection.close()
"""
