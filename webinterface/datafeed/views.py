from django.shortcuts import render
import picamera
import os
from django.http import HttpResponse

camera = picamera.PiCamera()

def index(request):
	return HttpResponse(camera.capture())
	#return HttpResponse("hello derp!")

def datafeed(request):
	camera.capture('derp.jpg')

	return HttpResponse(camera.capture())


# Create your views here.
