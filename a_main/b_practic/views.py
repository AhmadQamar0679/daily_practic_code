from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Courses


# Create your views here.

def home(request):
    if request.method == 'POST':
        data=request.POST
        course_name=data.get("course_name")
        course_description=data.get('course_description')
        
        course_image=request.FILES.get("course_image")    
        Courses.objects.create(
            course_name=course_name,
            course_description=course_description,
            course_image=course_image,
            

        )
        return redirect("/")
    return render(request,'home.html')


def course(request):
    queryset=Courses.objects.all()
    context = {'courses':queryset} 
    return render(request,'courses.html',context)

def delete_course(request,id):
    queryset=Courses.objects.get(id=id)
    queryset.delete()
    return redirect('/course/')





def about(request):
    return render(request,'about.html')
