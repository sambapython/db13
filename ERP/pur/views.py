from django.shortcuts import render

# Create your views here.
def pur_view_index(request):
	return render(request,"pur/index.html")
