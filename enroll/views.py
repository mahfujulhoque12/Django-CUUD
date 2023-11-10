from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentsRegestration
from .models import User
# Create your views here.
def add_show(request):
 
    if request.method== "POST":
        fm=StudentsRegestration(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pas=fm.cleaned_data['password']
            reg=User(name=nm,email=em,password=pas)
            reg.save()
            fm=StudentsRegestration()   
    else:
        fm=StudentsRegestration()    
    stud=User.objects.all() 
    return render(request,'enroll/addandshow.html',{'form':fm,'stu':stud})


# updataFunction
def update_data(request,id):
    if request.method == "POST":
        pi=User.objects.get(pk=id)
        fm=StudentsRegestration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi=User.objects.get(pk=id)
        fm=StudentsRegestration(instance=pi)        
    return render(request,'enroll/update.html',{'form':fm})

# deleteFunctio
def delete_data(request,id):
    if request.method=="POST":
        pi=User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
        
    