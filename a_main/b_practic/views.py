from django.shortcuts import render,redirect

from .models import *

# Create your views here.

def home(request):
    if request.method == 'POST':
        data=request.POST
        first_name=data.get("first_name")
        last_name=data.get("last_name")
        Age=data.get("Age")
        print("first_name: ",first_name)
        print("last_name: ",last_name)
        print("Age: ",Age)
    
        User.objects.create(
            first_name=first_name,
            last_name=last_name,
            Age=Age,
            

        )
        return redirect("/")
    
    return render(request,'home.html')

def course(request):
    return render(request,'courses.html')


def about(request):
    return render(request,'about.html')
