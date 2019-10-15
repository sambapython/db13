from django.shortcuts import render
from info.models import ReqTrack
class ReqCheck:
	def __init__(self, view):
		self.view=view
	def __call__(self,request):		
		meta = request.META
		req = ReqTrack(ip=meta.get("REMOTE_ADDR"),url=meta.get("PATH_INFO"))
		req.save()
		resp = self.view(request)

		#error handling
		staus_code=resp.status_code
		req.resp_status_code=staus_code
		req.save()
		if staus_code==404:
			return render(request, "info/404.html")
		elif staus_code==500:
			return render(request,"info/500.html")
		return resp