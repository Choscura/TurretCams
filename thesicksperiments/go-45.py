from pyax12.connection import Connection

# Connect to the serial port
serial_connection = Connection(port="/dev/ttyACM0", baudrate=1000000)

print("scanning")
# Ping the dynamixel unit(s)
ids_available = serial_connection.scan()

print("Scanned")
for dynamixel_id in ids_available:


      while True:
# Go to -45° (45° CW)
#serial_connection.goto(dynamixel_id, -45, speed=512, degrees=True)
#time.sleep(1)    # Wait 1 second
#serial_connection.goto(dynamixel_id, 45, speed=512, degrees=True)
#time.sleep(1)
# Close the serial connection
#serial_connection.close()

