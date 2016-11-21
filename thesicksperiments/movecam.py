from pyax12.connection import *
import time

print ("importing all")

# Connect to the serial port
serial_connection = Connection(port="/dev/ttyACM0", baudrate=57600)
print (serial_connection)
dynamixel_id = 0 

print("audit1")
# Go to 0
print(serial_connection.goto(dynamixel_id, 0))
time.sleep(1)    # Wait 1 second

print("audit2")
# Go to -45° (45° CW)
serial_connection.goto(dynamixel_id, -45, speed=512, degrees=True)
time.sleep(1)    # Wait 1 second

print("audit3")
# Go to -90° (90° CW)
serial_connection.goto(dynamixel_id, -90, speed=512, degrees=True)
time.sleep(1)    # Wait 1 second

print("audit4")
# Go to -135° (135° CW)
serial_connection.goto(dynamixel_id, -135, speed=512, degrees=True)
time.sleep(1)    # Wait 1 second

print("audit5")
# Go to -150° (150° CW)
serial_connection.goto(dynamixel_id, -150, speed=512, degrees=True)
time.sleep(1)    # Wait 1 second

print("audit6")
# Go to +150° (150° CCW)
serial_connection.goto(dynamixel_id, 150, speed=512, degrees=True)
time.sleep(2)    # Wait 2 seconds

print("audit7")
# Go to +135° (135° CCW)
serial_connection.goto(dynamixel_id, 135, speed=512, degrees=True)
time.sleep(1)    # Wait 1 second

print("audit8")
# Go to +90° (90° CCW)
serial_connection.goto(dynamixel_id, 90, speed=512, degrees=True)
time.sleep(1)    # Wait 1 second

print("audit9")
# Go to +45° (45° CCW)
serial_connection.goto(dynamixel_id, 45, speed=512, degrees=True)
time.sleep(1)    # Wait 1 second

print("audit10")
# Go back to 0°
serial_connection.goto(dynamixel_id, 0, speed=512, degrees=True)

# Close the serial connection
serial_connection.close()
