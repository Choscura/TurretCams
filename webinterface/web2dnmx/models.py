from __future__ import unicode_literals

from django.db import models

from dxl.dxlchain import DxlChain

class connection(models.Model):
	"""
	the "connection" class object instance represents the collection of motors assembled into a coherent unit,
	as it would be experienced by the computer program looking for sensor data.
	"""
	def __init__(self):
		pass
