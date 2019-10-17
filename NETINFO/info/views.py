from django.shortcuts import render
from django.http import HttpResponse
import logging
logger = logging.getLogger(__name__)

# # Create your views here.
# def view_gateways(request):
# 	return render(request,"info/gateways.html")
def index_view(request):
	logger.info("info this is index view")
	logger.debug("debug this is index view")
	logger.warning("warning is index view")
	logger.error("error this is index view")
	return render(request,"info/index.html")
def view_routers(request):
	return HttpResponse("name: Admin router,ip:192.0.0.1")

def view_hosts(request):
	# render will read the html code from the file mentioned, will create HttpResponse object with it.
	return render(request, "index.html")