from django.shortcuts import render

# Create your views here.
def sales_view_index(request):
	return render(request,"sales/index.html")
