from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def view_gateways(request):
	return HttpResponse("hello")
def view_routers(request):
	return HttpResponse("name: Admin router,ip:192.0.0.1")

def view_hosts(request):
	resp = """
	<html>
	<h1> Name: my compter,ip:192.168.250.1</h1>
	</html>
	"""
	return HttpResponse(resp)