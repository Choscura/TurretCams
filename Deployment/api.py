from pyax12.connection import Connection

# Connect to the serial port
serial_connection = Connection(port="/dev/ttyACM0", baudrate=57600)

dxlid = 1

# Print the control table of the specified Dynamixel unit
serial_connection.pretty_print_control_table(dxlid)

# Close the serial connection
serial_connection.close()
