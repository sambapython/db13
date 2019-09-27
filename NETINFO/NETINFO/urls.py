"""NETINFO URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from django.http import HttpResponse
from info.views import view_routers, view_hosts, index_view
from info.gateway_views import create_gateway_view, view_gateways,\
update_gateway_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",index_view),
    path('gateways/',view_gateways), # this view_gateways call by sever by passing request object as an argument.
    path("routers/", view_routers),
    path("hosts/",view_hosts),
    path("create_gateway",create_gateway_view),
    re_path("update_gateway/(?P<pk>[0-9]+)", update_gateway_view) #update_gateway_view(req_obj,pk=3)
]
