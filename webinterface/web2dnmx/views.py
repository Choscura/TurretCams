from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
import os, sys
from dxl.dxlchain import DxlChain
import logging 			#Logging to identifyproblems!

import datetime

logger = logging.getlogger(__name__)

def current_datetime(request):
	now = datetime.datetime.now()	
	chain=DxlChain("/dev/ttyACM0", rate=57600, timeout=0.1)

	motors = chain.get_motor_list()
	try:
		sync_write_pos_speed([1,2][500,500],[50,300])
	except error e:
		logger.error(e)
	


	derp = "<html><body>motors now contains %s</body></html>" %motors # %strung 
	return HttpResponse(derp)

"""


def motor_controller(View):
	if request.method == 'GET':
		pass
		return HttpResponse(html)	
	elif request.method == 'POST':
		pass
"""			
