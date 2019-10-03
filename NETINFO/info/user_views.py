from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
def signup(request):
	msg=""
	if request.method=="POST":
		data=request.POST
		username=data.get("username")
		password=data.get("password")
		try:
			user = User(username=username,password=password)
			user.save()
			user.set_password(password)
			user.save()
			msg="Signup done successfully"
		except Exception as err:
			msg=str(err)+" Username %s allready exist"%(username)
	return render(request,"info/signup.html",
	{"message":msg})
def signin(request):
	msg=""
	if request.method=="POST":
		data=request.POST
		username=data.get("username")
		password=data.get("password")
		user=authenticate(username=username,password=password)
		if user:
			login(request,user)
			msg="signin successfully"
		else:
			msg="wrong username and password"
	return render(request,"info/signin.html",{"message":msg})
def signout(request):
	logout(request)
	return redirect("/")