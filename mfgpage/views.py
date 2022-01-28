from multiprocessing import Manager
from django.shortcuts import render,HttpResponseRedirect
from .forms import mfg_config
from .models import user
from django.contrib.auth.models import Group,User
# Create your views here.

def home(request):
    return render(request,'nav.html')

def configuration(request):
    return render(request,'configurations.html')

# def home(request):
#     return render(request,'base.html')


    #this function will add new item and show all item
def add_show(request):
    fm  = {}
    if request.method=='POST':

        fm=mfg_config(request.POST,request.FILES)
        if fm.is_valid():
            user=fm.save()
            group=Group.objects.get(name='manager')
            user.groups.add(group)
    else:
        fm=mfg_config()
    stud=user.objects.all()
    img= user.objects.all()
        # return render(request,'addshow.html',{'form':fm})
    return render(request,'addshow.html',{'form':fm,'stu':stud,})

#this function will delete data
def delete_data(request,id):
    if request.method=="POST":
        pi=user.objects.get(pk=id)
        pi.delete()
        
    return HttpResponseRedirect('/')

    #function for updating data
def update_data(request,id):
    if request.method=="POST":
        pi=user.objects.get(pk=id)
        fm=mfg_config(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
        # else:
        #     pi=user.objects.get(pk=id)
        #     fm=StudentRegistration(intsance=pi)

    return render(request,'update.html',{'id':id})

# def searchbar(request):
#              if q in request.GET:
#         q.request.GET['q']
#         posts=user.objects.filter(name=q)

#     else:
#         posts=user.objects.all()

    # search=request.GET.get('search')
    # post=user.objects.all().filter(name=search)
    return render(request,'addshow.html',{'post':post})    