from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from info.models import Gateway,Vlan
from rest_framework.serializers import ModelSerializer
from rest_framework import status, viewsets

# Create your views here.
class VlanSerializer(ModelSerializer):
	class Meta:
		model=Vlan 
		fields = "__all__"
class VlanViewSet(viewsets.ModelViewSet):
	queryset  = Vlan.objects.all()
	serializer_class=VlanSerializer
	

class GateWaySerializer(ModelSerializer):
	class Meta:
		model = Gateway
		#fields = "__all__"
		exclude = ["create_date"]
class GateWayPutSerializer(ModelSerializer):
	class Meta:
		model = Gateway
		fields="__all__"
		#exclude = ["create_date"]
		extra_kwargs={"ip":{"required":False},
		"name":{"required":False},
		"mask":{"required":False},
		"interface_name":{"required":False},
		"route":{"required":False}}
		
class GateWayView(APIView):
	def get(self,request,pk=None):
		if pk:
			data = Gateway.objects.filter(pk=pk)
		else:
			data = Gateway.objects.all()
		ser = GateWaySerializer(data,many=True)
		#data = [{"name":row.name,"ip":row.ip} for row in data]
		return Response(ser.data)

	def post(self,request):
		data=request.data
		ser = GateWaySerializer(data=data)
		if ser.is_valid():
			ser.save()
			return Response({"status":"success","data":ser.data,"errors":{}},
				status = status.HTTP_201_CREATED)
		else:
			return Response({"status":"Failed","errors":ser._errors,"data":{}},
				status=status.HTTP_400_BAD_REQUEST)
	def put(self,request,pk):
		gateways = Gateway.objects.filter(pk=pk)
		if gateways:
			ser=GateWayPutSerializer(data=request.data,instance=gateways[0])
			if ser.is_valid():
				ser.save()
				return Response({"status":"success","data":ser.data})
			else:
				return Response({"status":"Failed","errors":ser._errors,"data":{}},
					status=status.HTTP_400_BAD_REQUEST)
		else:
			return Response({"status":"failed","data":{},
				"errors":["gateway not found with the given id:%s"%pk]},
				status=status.HTTP_404_NOT_FOUND)
	def delete(self,request,pk):
		gateways = Gateway.objects.filter(pk=pk)
		if gateways:
			gateway = gateways[0]
			gateway.delete()
			return Response({"status":"success","data":{"id":pk}})
		else:
			return Response({"status":"failed","data":{},
				"errors":["gateway not found with the given id:%s"%pk]},
				status=status.HTTP_404_NOT_FOUND)

