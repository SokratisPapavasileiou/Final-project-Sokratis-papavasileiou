from django.shortcuts import render, redirect

from .forms import NewUserForm
from .models import *
from django.http.response import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
def first(request):
    
    return render(request, "first/firstprojectwebpage.html",)
def inp(request):
   names = menu.objects.all()
   output = {'name':names}
   
   return render(request, "first/menus.html",output,
    
    )
def tests(request):
   jaja = test2.objects.all()
   output = {'name':jaja}
   return render(request, "first/menus.html",output,
    
    )

def menudata(request):
    return render(request, "first/menudata.html",)

@login_required(login_url='userdata' )
def about(request):
    rate= userating.objects.all()
    output = {'rate':rate}
    return render(request, "first/about.html",output)
    

def logins(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password=request.POST["password"]
        
        user = authenticate(request, username=username,email=email, password=password)
        
        

        if user is not None:
            login(request,user)
           
            
            return HttpResponseRedirect(reverse("firstprojectwebpage"), {
                "message" : "login successfull"
            }  )
        else:
            return render(request, "first/userdata.html", {
                "message" : "Invalid data"
            })
    else:
        return render(request, "first/userdata.html",{
                "message" : "Invalid data"
            })

def logouts(request):
    logout(request)
    return render(request, "first/userdata.html", {
        "message" : "Logout"
    })
def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request,user)
			messages.success(request, "Registration successful." )
			return redirect("first/firstprojectwebpage.html")
		messages.error(request, "Unsuccessful registration.")
	form = NewUserForm()
	return render (request=request, template_name="first/firstprojectwebpage.html", context={"register_form":form})
def registretionmesage(request):
    return render(request, "first/registretionmesage.html",)





def search(request):
    
    if  request.method == "POST":
        
        searchbar = request.POST["searchbar"]
        all=menu.objects.filter(name__contains=searchbar)
        
        return render (request,"first/menus.html",{'all':all})

    else:
        
        return render (request,"first/menus.html",)



