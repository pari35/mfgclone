from enum import auto
from django.shortcuts import redirect, render ,HttpResponse,HttpResponseRedirect
from .forms import Connector,MfgConnector
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,'home.html')
    
def amenities(request):
    return render(request,'amenity.html',)

def configurations(request):
    return render(request,'configurations.html')

def connector(request):
    if request.method=='POST':
        # con=Connector(request.POST,request.FILES)
        con=Connector(type=request.POST["type"], name=request.POST["name"])
        
        # print(request.POST, request.FILES)
        # print(con)
        # if con.is_valid():
        # C=Connector.objects.all()
        con.save()
    con=Connector.objects.all()

        # else:
            # con=Connector()
        # return render(request,'modal.html',{'form':con})
        
    return render(request,'modal.html',{'con':con})


#this function will delete data
def delete_data(request):
    
    if request.method=="POST":

        # Connector.objects.filter(id=request.POST.get("id")).first().delete()
        Connector.objects.get(id=request.POST.get("id")).delete()
        # print(delet)
        # delet.delete()
    return HttpResponseRedirect('connector')
    # return render(request,'modal.html')

#Registration of admin
def register(request):
    if request.method=="POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
    # if email.objects.filter(email=email).extists():
    #     messages.info(request,'Username Taken')
        admin_reg=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,password=password,email=email)
        admin_reg.save()
        messages.info(request,"Registration succesfull !!")
    return render(request,'registration.html')

def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        print("Authenticated")
        
        if user is not None:
            auth.login(request,user)

        return redirect("home")
    else:
        messages.info(request,'Invalid Credential')

    return render(request,'admin_login.html')