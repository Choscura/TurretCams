from __future__ import unicode_literals


from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

class ax12a(models.Model):
	pass

class connection(models.Model):
	def open(self, port, baudrate, timeout, waiting_time):
		pass
	
	def close(self):
		pass	

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

	bool has_angle_limit_alarm_led(self, dynamixel_id):
		pass

	bool has_angle_limit_alarm_shutdown(Self, dynamixel_id):	
		pass

	

class packet(models.Model):
	pass

class instruction_packet(models.Model):
	pass


class 
