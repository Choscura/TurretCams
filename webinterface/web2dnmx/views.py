from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from dxl.dxlchain import DxlChain

import datetime

def current_datetime(request):
	now = datetime.datetime.now()
    #chain=DxlChain("/dev/ttyACM0", rate=57142, timeout=0.1, waiting_time=0.02)
	#motors = chain.get_motor_list()
	#try:
	#		chain.sync_write_pos_speed([1,2][512,512],[512,512])"""
	page="<html><body>It is now %s</body></html>" %now
	
	return HttpResponse(page)


def motor_controller(View):
	if request.method == 'GET':
		pass
		return HttpResponse(html)	
	elif request.method == 'POST':
		pass
			
