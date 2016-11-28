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

	def open(self, _port, _baudrate, _timeout, _waiting_time):
		"""
		a connection opener for letting the web app actually open a connection to the motors connected to the server
		"""
		self.serialconnection = Connection(port = _port, baudrate=_baudrate, timeout = _timeout, waiting_time = _waiting_time)
		
		
	def close(self):
		self.serialconnection.close()

	def dump_control_table(self, dynamixel_id):
		pass

	def get_baud_rate(self, dynamixel_id):
		pass

	 def get_ccw_angle_limit(self, dynamixel_id):
		pass

	def  get_ccw_compliance_margin(self, dynamixel_id):
		pass

	def  get_ccw_compliance_slope(self, dynamixel_id):
		pass

	def  get_control_table_tuple(self, dynamixel_id):
		pass

	def  get_cw_angle_limit(self, dynamixel_id):
		pass

	def get_cw_compliance_margin(self, dynamixel_id):
		pass 
	
	def  get_cw_compliance_slope(self, dynamixel_id):
		pass

	def  get_down_calibration(self, dynamixel_id):
		pass

	def  get_firmware_version(self, dynamixel_id):
		pass

	def get_goal_position(self, dynamixel_id):
		pass

	def get_max_temperature(self, dynamixel_id):
		pass

	def get_max_torque(self, dynamixel_id):
		pass

	def get_max_voltage(self, dynamixel_id):
		pass

	def get_min_voltage(self, dynamixel_id):
		pass
	
	def get_mode_number(self, dynamixel_id):
		pass

	def get_moving_speed(self, dynamixel_id):
		pass

	def get_present_load(self, dynamixel_id):
		pass

	def get_present_position(self, dynamixel_id):
		pass

	def get_present_speed(self, dynamixel_id):
		pass

	def get_present_temperature(self, dynamixel_id):
		pass
	
	def get_present_voltage(self, dynamixel_id):
		pass

	def get_punch(self, dynamixel_id):
		pass

	def get_return_delay(sef, dynamixel_id):
		pass

	def get_status_return_level(self, dynamixel_id):
		pass

	def get_torque_limit(self, dynamixel_id):
		pass

	def get_up_calibration(self, dynamixel_id):
		pass

	def	goto(self, dynamixel_id, position, speed, degree_boolean):
		pass
	
	has_angle_limit_alarm_led= models.BooleanField(Field.default=False)

	has_angle_limit_alarm_shutdown = models.BooleanField(Field.default=False)
	
	has_checksum_alarm_shutdown = models.BooleanField(Field.default=False)

	has_input_voltage_alarm_led = models.BooleanField(Field.default=False)

	has_input_voltage_alarm_shutdown = models.BooleanField(Field.default=False)

	has_instruction_alarm_led = models.BooleanField(Field.default=False)

	has_instruction_alarm_shutdown = models.BooleanField(Field.default=False)

	has_overheating_alarm_led = models.BooleanField(Field.default=False)

	has_overheating_alarm_shutdown = models.BooleanField(Field.default=False)

	has_overload_alarm_led= models.BooleanField(Field.default=False)

	has_overload_alarm_shutdown = models.BooleanField(Field.default=False)

	has_range_alarm_led = models.BooleanField(Field.default=False)

	has_range_alarm_shutdown = models.BooleanField(Field.default=False)

	has_registred_instruction = models.BooleanField(Field.default=False)

	is_led_enabled = models.BooleanField(Field.default=False)

	is_locked = models.BooleanField(Field.default=False)

	is_moving = models.BooleanField(Field.default=False)

	is_torque_enabled = models.BooleanField(Field.default=False)

	

class packet(models.Model):
	checksum = models.BinaryField(Field.Default=False)
	

class instruction_packet(models.Model):
	pass


class 
