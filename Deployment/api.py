"""
Iunu Dynamixel API!

This API wraps up the pyax12 library for talking to Dynamixel ax12a servo motors
over a USB2AX usb plug.  Everything in this file is hard-coded to deal with a turret
that is based on a raspberry pi 3 model B, running 2 dynamixel ax12a servos. Your
mileage on different systems using different architectures will vary..

"""

# Connection handling

#This is worth saying twice- connections are a BIG FUCKING DEAL, they are difficult
#things to manage, and special handling is needed to make them reliable
from pyax12.connection import Connection

serial_connection = Connection(port="/dev/ttyACM0", baudrate = 57600)

def replug_connect():
    for x in range(0,10):
        try:
            Port = "/dev/ttyACM" + str(x)
            serial_connection = Connection(port = Port, baudrate = 57600)
        except SerialException:
            return "current generation of game-stopping error. Physically reset."


#TODO: error handling on a TypeError where a '0' is being returned as possibly a 'Null' or 'False'.
# dxlid = int(0 not False)







# Print the control table of the specified Dynamixel unit
serial_connection.pretty_print_control_table(1)

# Close the serial connection
serial_connection.close()
