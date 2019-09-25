from django.db.utils import IntegrityError
from django.shortcuts import render, redirect
from info.models import Gateway
from info.forms import GatewayForm
# Create your views here.
def update_gateway_view(request,pk):
	msg=""
	gateways = Gateway.objects.filter(pk=pk)
	if gateways:
		gateway=gateways[0]
		if request.method=="POST":
			new_data = request.POST
			form = GatewayForm(new_data,instance=gateway)
			if form.is_valid():
				form.save()
				msg="Gateway Updated successfully!!"
				return redirect("/gateways")
			else:
				msg=form._errors
		else:
			form = GatewayForm(instance=gateway)

	else:
		form = GatewayForm()
		msg="gateways are not found"
	return render(request,"info/create_gateway.html",
		{"form":form,"message":msg})

def view_gateways(request):
	gateways = Gateway.objects.all()
	return render(request,"info/gateways.html",{"data":gateways})
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
				return redirect("/gateways")
			else:
				msg=form._errors
			
		except IntegrityError as err:
			msg=str(err)
		except Exception as err:
			msg=str(err)
	if request.method=="GET":
		form = GatewayForm()
	return render(request,"info/create_gateway.html",{"message":msg,"form":form})

