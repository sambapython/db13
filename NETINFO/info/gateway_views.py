from django.db.utils import IntegrityError
from django.shortcuts import render
from info.models import Gateway
from info.forms import GatewayForm
def create_gateway_view(request):
	msg=""
	if request.method == "POST":
		data=request.POST
		# gwi  = Gateway(name=data.get("name"),
		# 	ip=data.get("ip"),
		# 	mask=data.get("mask"),
		# 	route = data.get("route"),
		# 	interface_name=data.get("interface"))
		try:
			#gwi.save()
			form = GatewayForm(data=request.POST)
			if form.is_valid():
				form.save()
				msg="Gateway created successfully"
			else:
				msg=form._errors
			
		except IntegrityError as err:
			msg=str(err)
		except Exception as err:
			msg=str(err)
	if request.method=="GET":
		form = GatewayForm()
	return render(request,"info/create_gateway.html",{"message":msg,"form":form})

