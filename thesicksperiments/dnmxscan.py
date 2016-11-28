
from pyax12.connection import Connection

# Connect to the serial port
serial_connection = Connection(port="/dev/ttyACM0", baudrate=100000)

print("scanning")
# Ping the dynamixel unit(s)
ids_available = serial_connection.scan()

print("Scanned")
for dynamixel_id in ids_available:
	print(dynamixel_id)
	
	print("control tabling")
	serial_connection.pretty_print_control_table(dynamixel_id)
#print("serial connection tried to print control table, nothing happened")

# Close the serial connection
serial_connection.close()

"""


from pyax12.connection import Connection

# Connect to the serial port
serial_connection = Connection(port="/dev/ttyACM0", baudrate=57600)

dynamixel_id = 1

# Print the control table of the specified Dynamixel unit
serial_connection.pretty_print_control_table(dynamixel_id)

# Close the serial connection
serial_connection.close()"""
