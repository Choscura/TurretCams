from flask import Flask, jsonify
import time
#from random import randint			# 	testing byproduct, not actually used in deployment
from pyax12.connection import Connection
 
connection = Connection(port="/dev/ttyACM0", baudrate=1000000, timeout=0.2, waiting_time=0.02)

def connect():
	"""
	serial connection handling
	"""
	dxl1=1
	dxl2=2
	connection.pretty_print_control_table(dxl1)
	for i in range(3):
		connection.goto(1,512)
		connection.goto(2, 512)
		#connection.goto(1, 300)
		print(connection.ping(2)) #%(x for x in range 100)
	
def close_connection():
	connection.close()	

def get_position():
	return connection.get_present_position()	

def Set_relative_position():
	pass

def set_absolute_positon():
	pass

def center():
	connection.goto(1,512)
	connection.goto(2,512)


#flask-specific things and API code

close_connection()

app = Flask(__name__)

@app.route('/')
def index():
	center()
	return "%s" %motors

if __name__ == '__main__':
	app.run(debug=True, host="172.25.1.182", port=8000)

