from __future__ import unicode_literals

#pyax12 imports for motor control
from pyax12.connection import Connection

#Django native/default imports
from django.db import models

#Django admin imports
from django.contrib import admin


#Serializer and API imports
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

class ax12a(models.Model):
	pass



"""
Connection class: the connection handles the actual controls of, input to, and output from the motors
"""
class connection(models.Model):
	#member data
		
	has_angle_limit_alarm_led			= models.BooleanField(Field.default=False)
	has_angle_limit_alarm_shutdown 		= models.BooleanField(Field.default=False)
	has_checksum_alarm_shutdown 		= models.BooleanField(Field.default=False)
	has_input_voltage_alarm_led 		= models.BooleanField(Field.default=False)
	has_input_voltage_alarm_shutdown 	= models.BooleanField(Field.default=False)
	has_instruction_alarm_led 			= models.BooleanField(Field.default=False)
	has_instruction_alarm_shutdown 		= models.BooleanField(Field.default=False)
	has_overheating_alarm_led 			= models.BooleanField(Field.default=False)
	has_overheating_alarm_shutdown 		= models.BooleanField(Field.default=False)
	has_overload_alarm_led				= models.BooleanField(Field.default=False)
	has_overload_alarm_shutdown 		= models.BooleanField(Field.default=False)
	has_range_alarm_led 				= models.BooleanField(Field.default=False)
	has_range_alarm_shutdown 			= models.BooleanField(Field.default=False)
	has_registred_instruction 			= models.BooleanField(Field.default=False)
	is_led_enabled 						= models.BooleanField(Field.default=False)
	is_locked 							= models.BooleanField(Field.default=False)
	is_moving 							= models.BooleanField(Field.default=False)
	is_torque_enabled 					= models.BooleanField(Field.default=False)
	
	#member functions for native django functionality
	
	def __tostring__():
		pass


	#member functions for motor control and interaction


	#member functions for API controls and interactions

	def open(self, _port, _baudrate, _timeout, _waiting_time):
		"""
		a connection opener for letting the web app actually open a connection to the motors connected to the server
		"""
		# the Connection object is a dynamically generated, since it's a python class that isn't natively serializable
		self.serialconnection = Connection(port = _port, baudrate=_baudrate, timeout = _timeout, waiting_time = _waiting_time)
		
	
	# the close function that is part of the disposal of the connection class object instances.	
	def close(self):
		self.serialconnection.close()

	# a function to print out all of the data available by the motor for the purposes of diagnostics
	def dump_control_table(self, dynamixel_id):
		return str(self.serialconnection.dump_control_table(dynamixel_id))

	def get_baud_rate(self, dynamixel_id):
		return str(self.serialconnection.get_baud_rate(self, dynamixel_id))

	 def get_ccw_angle_limit(self, dynamixel_id):
		return str(self.serialconnection.get_ccw_angle_limit(self, dynamixel_id))

	def  get_ccw_compliance_margin(self, dynamixel_id):
		return str(self.serialconnection.get_ccw_compliance_margin(self, dynamixel_id))

	def  get_ccw_compliance_slope(self, dynamixel_id):
		return str(self.serialconnection.get_ccw_compliance_slope(self, dynamixel_id))

	def  get_control_table_tuple(self, dynamixel_id):
		return str(self.serialconnection.get_control_table_tuple(self, dynamixel_id))

	def  get_cw_angle_limit(self, dynamixel_id):
		return str(self.serialconnection.get_cw_angle_limit(self, dynamixel_id))

	def get_cw_compliance_margin(self, dynamixel_id):
		return str(self.serialconnection.get_cw_compliance_margin(self, dynamixel_id))
	
	def  get_cw_compliance_slope(self, dynamixel_id):
		return str(self.serialconnection.get_cw_compliance_slope(self, dynamixel_id))

	def  get_down_calibration(self, dynamixel_id):
		return str(self.serialconnection.get_down_calibration(self, dynamixel_id))

	def  get_firmware_version(self, dynamixel_id):
		return str(self.serialconnection.get_firmware_version(self, dynamixel_id))

	def get_goal_position(self, dynamixel_id):
		return str(self.serialconnection.get_goal_position(self, dynamixel_id))

	def get_max_temperature(self, dynamixel_id):
		return str(self.serialconnection.get_max_temperature(self, dynamixel_id))

	def get_max_torque(self, dynamixel_id):
		return str(self.serialconnection.get_max_torque(self, dynamixel_id))

	def get_max_voltage(self, dynamixel_id):
		return str(self.serialconnection.get_max_voltage(self, dynamixel_id))

	def get_min_voltage(self, dynamixel_id):
		return str(self.serialconnection.get_min_voltage(self, dynamixel_id))
	
	def get_mode_number(self, dynamixel_id):
		return str(self.serialconnection.get_mode_number(self, dynamixel_id))

	def get_moving_speed(self, dynamixel_id):
		return str(self.serialconnection.get_moving_speed(self, dynamixel_id))

	def get_present_load(self, dynamixel_id):
		return str(self.serialconnection.get_present_load(self, dynamixel_id))

	def get_present_position(self, dynamixel_id):
		return str(self.serialconnection.get_present_load(self, dynamixel_id))

	def get_present_speed(self, dynamixel_id):
		return str(self.serialconnection.get_present_speed(self, dynamixel_id))

	def get_present_temperature(self, dynamixel_id):
		preturn str(self.serialconnection.get_present_speed(self, dynamixel_id)
	
	def get_present_voltage(self, dynamixel_id):
		return str(self.serialconnection.get_present_speed(self, dynamixel_id))

	def get_punch(self, dynamixel_id):
		return str(self.serialconnection.get_present_speed(self, dynamixel_id))

	def get_return_delay(sef, dynamixel_id):
		return str(self.serialconnection.get_present_speed(self, dynamixel_id))

	def get_status_return_level(self, dynamixel_id):
		return str(self.serialconnection.get_present_speed(self, dynamixel_id))

	def get_torque_limit(self, dynamixel_id):
		return str(self.serialconnection.get_present_speed(self, dynamixel_id))

	def get_up_calibration(self, dynamixel_id):
		return str(self.serialconnection.get_present_speed(self, dynamixel_id))

	def	goto(self, dynamixel_id, position, speed, degree_boolean):
		return str(self.serialconnection.get_present_speed(self, dynamixel_id))
	



class packet(models.Model):
	"""	
	The general raw Packet class.

	It implements the either “instruction packet” (the packets sent by the controller 
	to the Dynamixel actuators to send commands) or “status packet” (the response packets 
	from the Dynamixel units to the main controller after receiving an instruction packet).

	The structure of a general Packet is as the following:

	0xFF 	0xFF 	ID 	LENGTH 	DATA... 	CHECK SUM

	This class has been made for debugging purpose and is not intended to be used widely 
	to create packets. Instead, it is recommanded to use InstructionPacket or StatusPacket 
	classes to build Packet instances.
	
	Parameters:	
    dynamixel_id 	(int) 	– 	the unique ID of a Dynamixel unit (from 0x00 to 0xFD), 
								0xFE is a broadcasting ID.

    data 			(bytes) – 	a sequence of byte containing the packet’s data: the 
								instruction to perform or the status of the Dynamixel 
								actuator. This data argument contains the fifth to the 
								penultimate byte of the full built packet.

	"""
	checksum 		= models.BinaryField(Field.Default=False)
	data 			= models.DataField()
	dynamixel_id 	= models.UniqueIdentifier()
	header 			= models.DataField()
	length 			= models.IntegerField()

	def to_byte_array(self):
		pass

	def to_bytes(self):
		pass

	def to_integer_tuple(self):
		pass

	def to_printable_string(self):
		pass

	def compute_checksum(self, bytesequence):
		pass

class instruction_packet(models.Model):
	pass



