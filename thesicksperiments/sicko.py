import time
from pyax12 import Connection



def connect():
	"""
	serial connection handling
	"""
	connection = Connection(port="/dev/ttyACM0", baudrate="1000000", timeout="0.1", waiting_time="0.02")

	
def close_connection():
	pass

def get_position():
	pass

def Set_relative_position():
	pass

def set_absolute_positon():
	pass


