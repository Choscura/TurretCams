# TurretCams

This is the readme for the Turret Camera project to run on raspberry pi 3 and control a 
turret camera mount system for taking automated graphical measurements of production
greenhouse environments for the Iunu company.


OVERVIEW

	physical architecture
		Nodes
			local servers
			raspberry pi 3 b+
		Networking
			Unifi Edge Router
			Unifi AP-LR
		actuators
			dynamixel ax12a
		sensors
			yoctopuce
			whitebox labs
	logical architecture
		API's
			camera
			other sensor
			actuator
			digested_data
			raw_data
	division of labor
