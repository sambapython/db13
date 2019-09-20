from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def view_gateways(request):
	return render(request,"gateways.html")
def view_routers(request):
	return HttpResponse("name: Admin router,ip:192.0.0.1")

def view_hosts(request):
	# render will read the html code from the file mentioned, will create HttpResponse object with it.
	return render(request, "index.html")