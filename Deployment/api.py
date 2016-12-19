"""
Iunu Dynamixel API!

This API wraps up the pyax12 library for talking to Dynamixel ax12a servo motors
over a USB2AX usb plug.  Everything in this file is hard-coded to deal with a turret
that is based on a raspberry pi 3 model B, running 2 dynamixel ax12a servos. Your
mileage on different systems using different architectures will vary..

"""

################################# Connection handling  ###########################################

#This is worth saying twice- connections are a BIG FUCKING DEAL, they are difficult
#things to manage, and special handling is needed to make them reliable
from pyax12.connection import Connection

serial_connection = Connection(port="/dev/ttyACM0", baudrate = 57600)

#this connection function is in case of error of the connection above, which SHOULD be fine
#But "SHOULD" is a fucking terrible garuntee.
def connect():
	try:
		#	flush the buffer of the connection and see if that allows it to reassert itself
		serial_connection.flush()
		try:  					#	try first with default port name (ttyACM0) before trying elsewhere
			serial_connection = Connection(port="/dev/ttyACM0", baudrate = 57600)
		except:					# 	current "elsewhere" definition confined to sequential suffix numbers
			for x in range (0,99):
				location_string = "/dev/ttyACM" + str(x)
				serial_connection = Connection (location_string, baudrate = 57600)
	except SerialException:		#	if everything's fucked:
		return "current generation of game-stopping error. Physically reset."


if not serial_connection.ping():
	connect()

#TODO: error handling on a TypeError where a '0' is being returned as possibly a 'Null' or 'False'.
# dxlid = int(0 not False)

####################################  MOTOR ACTIONS  ############################################
######	This section reserved for code pertaining to physical actions by motors 	#############

#goto- the workhorse
def goto(ID, position):
	serial_connection.goto(ID, position)

#synchronized goto- exists in dynamixel functions, but not yet discovered in pyax12 code? <may need to be written>
##  TODO  ##
def sync_goto():
	pass

###################################  GET Meta  ##################################################
#######	This section reserved for code pertaining to the data sent by the motor to the API ######

#Get Model #
def get_model_number(ID):
	return serial_connection.get_model_number(ID)

#Get Firmware version
def get_firmware_ver(ID):
	return serial_connection.get_firmware_version

# get baud rate
def get_baudrate(ID):	
	return serial_connection.get_baud_rate(ID)

# get return delay
def get_return_delay(ID):
	return serial_connection.get_return_delay_time(ID)

# get current angle limits

#	#	Clockwise
def get_clockwise_angle_limit(ID):
	return serial_connection.get_cw_angle_limit(ID)

#	#	counter-clockwise
def get_counterclockwise_angle_limit(ID):
	return serial_connection.get_ccw_angle_limit(ID)

# get punch
def get_punch(ID):
	return serial_connection.get_punch(ID)

# get status return level
def get_status_level(ID):
	"""
	due to complexity the docstring from the pyax12 code is copied here to explain basic paradigms

	This function reveals whether the specified Dynamixel unit is configured to return a
        *Status Packet* after receiving an *Instruction Packet*.

        +----------------+----------------------------------------+
        | Returned value | Meaning                                |
        +================+========================================+
        | 0              | Do not respond to any instructions     |
        +----------------+----------------------------------------+
        | 1              | Respond only to READ_DATA instructions |
        +----------------+----------------------------------------+
        | 2              | Respond to all instructions            |
        +----------------+----------------------------------------+

        :param int dynamixel_id: the unique ID of a Dynamixel unit. It must be
            in range (0, 0xFD).
	"""
	return serial_connection.get_status_return_level(ID)

# get lock status (returns BOOLEAN)
def get_lock_status(ID):
	return serial_connection.is_locked(ID)

# get movement status (returns BOOLEAN)
def get_movement_status(ID):
	return serial_connection.is_moving(ID)

# get instruction status (returns BOOLEAN)
def get_instruction_status(ID):
	return serial_connection.has_registered_instruction(ID)


#	#	#	#	#	 get MINIMUMS	#	#	#	#	#

	#Voltage
def get_min_volts(ID):
	return serial_connection.get_min_voltage(ID)

# 	#	#	#	#	get MAXIMUMS	#	#	#	#	#

	#Torque
def get_max_torque(ID):
	return serial_connection.get_max_torque(ID)


	#temp
def get_max_temp(ID):
	return serial_connection.get_max_temperature(ID)
	
	#Voltage
def get_max_volts(ID):
	return serial_connection.get_max_voltage(ID)


##################################  SET Meta  ###################################################
#set clockwise angle limit (dynamixel motor ID, limiting position, boolean of whether or not to calculate the position as an explicit motor position identity <ie, the 0-1023 range of positions the ax12a can move between> or as an angle (150 degrees of motion, ~.3 degrees per position)
def set_clockwise_limit(ID, limit, degrees):
	serial_connection.set_cw_angle_limit(ID, limit, degrees)

#set counterclockwise angle limit (see notes above on the clockwise variant of this)
def set_counterclockwise_limit(ID, limit, degrees):
	serial_connection.set_ccw_angle_limit(ID, limit, degrees)

# Print the control table of the specified Dynamixel unit
def prettyprint(ID):
	return serial_connection.pretty_print_control_table(ID)

# Close the serial connection
def close():
	serial_connection.close()
