from django.shortcuts import render
from django.views import View

def motor_controller(View):
	if request.method == 'GET':
		return HttpResponse('result')
