from django.shortcuts import render,redirect

from .models import Courses
# from .models import Courses

# Create your views here.

def home(request):
    if request.method == 'POST':
        data=request.POST
        course_name=data.get("course_name")
        course_description=data.get('course_description')
        course_image=request.FILES.get("course_image")
        # Age=data.get("Age")
        # print("course_name: ",course_name)
        # print("course_image: ",course_image)
        # print("Age: ",Age)
    
        Courses.objects.create(
            course_name=course_name,
            course_description=course_description,
            course_image=course_image,
            # Age=Age,
            

        )
        return redirect("/")
    
    return render(request,'home.html')

def course(request):
    # if request.method=='POST':
    #     data=request.POST
    #     course_name=data.get("course_name")
    #     course_image=request.FILES.get('course_name')
    #     Courses.objects.create(
    #         course_name=course_name,
    #         course_image=course_image,

        # )

        # return redirect('/course/')


    return render(request,'courses.html')


def about(request):
    return render(request,'about.html')
