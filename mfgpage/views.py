from django.shortcuts import render
from matplotlib import use
from .forms import mfg_config
from .models import user

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

        fm=mfg_config(request.POST)
        if fm.is_valid():
            fm.save()

    else:
        fm=mfg_config()
    stud=user.objects.all()
        # return render(request,'addshow.html',{'form':fm})
    return render(request,'addshow.html',{'form':fm,'stu':stud})