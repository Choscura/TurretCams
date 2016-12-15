from pyax12.connection import Connection

conn = Connection(port="/dev/ttyACM0", baudrate= 57600)

dxlid = 1

print(conn.ping(1))

#conn.pretty_print_control_table(dxlid)

conn.close()
