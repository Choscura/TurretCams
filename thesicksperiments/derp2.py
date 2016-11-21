import time
import math
from pyax12.connection import Connection
from pyax12.utils import degrees_to_dxl_angle

def degrees_to_dxl_angle(angle_degrees):
    """Normalize the given angle.

    PxAX-12 uses the position angle (-150.0°, +150.0°) range instead of the
    (0°, +300.0°) range defined in the Dynamixel official documentation because
    the former is easier to use (especially to make remarkable angles like
    right angles or 45° and 135° angles).

    :param float angle_degrees: an angle defined in degrees the range
        (-150.0°, +150.0°) where:

        - -150.0 is a 150° clockwise angle;
        - +150.0 is a 150° counter clockwise angle.

    :return: an angle defined according to the Dynamixel internal notation,
        i.e. in the range (0, 1023) where:

        - 0 is a 150° clockwise angle;
        - 1023 is a 150° counter clockwise angle.

    :rtype: int.
    """
    dxl_angle = math.floor((angle_degrees + 150.0) / 300. * 1023.)
    return dxl_angle

def main(*args):
	# Connect to the serial port
	serial_connection = Connection(port="/dev/ttyACM0", baudrate=1000000, timeout=0.1, waiting_time=0.02)

	print("scanning")
	# Ping the dynamixel unit(s)
	ids_available = serial_connection.scan()

	print("Scanned")
	for dynamixel_id in ids_available:

		counter =0
		

		while counter<60:
			# Go to -45 (45 CW)
			serial_connection.goto(dynamixel_id, degrees_to_dxl_angle(counter), speed=1024, degrees=False)

			time.sleep(1)    # Wait 1 second
			serial_connection.goto(dynamixel_id, degrees_to_dxl_angle(-(counter)), speed=768, degrees=False)
			time.sleep(1)
			counter += 1


	# Close the serial connection
	serial_connection.close()


main()
