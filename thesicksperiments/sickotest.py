import time
from pyax12.connection import Connection

def connect():
	"""
	serial connection handling
	"""
	dxl2 = 2
	connection = Connection(port="/dev/ttyACM0", baudrate=1000000, timeout=0.2, waiting_time=0.02)
	dxl1 = 1 
	connection.pretty_print_control_table(int(dxl1))
	#print(connection.ping(2)) #%(x for x in range 100)
 
def close_connection():
	pass

def get_position():
	pass
 
def Set_relative_position():
	pass

def set_absolute_positon():
	pass

connect()

