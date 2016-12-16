from flask import Flask, jsonify
import time
from random import randint			# 	testing byproduct, not actually used in deployment
from pyax12.connection import Connection
 
connection = Connection(port="/dev/ttyACM0", baudrate=100000, timeout=0.2, waiting_time=0.02)

#connection.goto(1,0)

if connection.ping(1)==False:
	print("derp")

@app=Flask(__name__)
@app.route('/connect')
def connect():
	#connection=Connection(port="/dev/ttyACM0", baudrate = 100000, timeout = 0.2, waiting_time = 0.02)
	"""
	serial connection handling
	"""
	dxl1=1
	dxl2=2
	cccombo = ""
	while cccombo == "" or None or Null or 0:
		try:
			connection.close()
			connection = Connection(port="/dev/ttyACM0", baudrate = 57600, timeout = 0.2, waiting_time= 0.02)
			cccombo+=(str(connection.pretty_print_control_table(dxl1) + str(connection.pretty_print_control_table(dxl2))))
		except:
			pass
	return cccombo
	#	connection.goto(1,512)
	#	connection.goto(2, 512)
	#	#connection.goto(1, 300)
	#	print(connection.ping(2)) #%(x for x in range 100)
	#return cccombo

#app = Flask(__name__)

@app.route('/close')	
def close_connection():
	constatus = str(connection.ping(1))
	connection.close()	
	terr = "motor1 con status"
	return jsonify(terr = constatus)


@app.route('/gorand')
def gorand():
	derp=randint(0,1023)
	connection.goto(1, derp)
	strong = str(connection.ping(1))
	derp = randint(0,1023)
	connection.goto(2, derp)
	strung = str(connection.ping(2))
	return "<html><head></head><body><h>" + strong + strung + "</h></body></html>"


def motors():
	r_string = str(connection.ping(1)) + str(connection.ping(2))
	return r_string

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

#close_connection()

#app = Flask(__name__)


@app.route('/')
def index():
	gorand()
	center()
	return "%s" %motors

if __name__ == '__main__':
	app.run(debug=True, host="172.25.1.182", port=8000)

