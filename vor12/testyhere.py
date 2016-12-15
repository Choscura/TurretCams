from pyax12.connection import Connection

conn = Connection(port="/dev/ttyACM0", baudrate=57600)

print (conn.ping(1))

print (conn.ping(8))

#print (conn.pretty_print_control_table())
