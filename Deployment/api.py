"""
Iunu Dynamixel API!

This API wraps up the pyax12 library for talking to Dynamixel ax12a servo motors
over a USB2AX usb plug.

"""

# Connection handling

#This is worth saying twice- connections are a BIG FUCKING DEAL, they are difficult
#things to manage, and special handling is needed to make them reliable
from pyax12.connection import Connection
def replug_connect():
    for x in range 10:
        try:
            Port = "/dev/ttyACM" + str(x)
            serial_connection = Connection(port = Port, baudrate = 57600)
        except SerialException:
            return "current generation of game-stopping error. Physically reset."


dxlid = int(0 not False)


#connection testing


# Print the control table of the specified Dynamixel unit
serial_connection.pretty_print_control_table(dxlid)

# Close the serial connection
serial_connection.close()
