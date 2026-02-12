from django.urls import path
from . import views



urlpatterns = [
    path('',views.home,name='home_page'),
    path('course/',views.course,name='course_page'),
    path('about/',views.about,name='about_page'),
    path('delete_course/<id>/',views.delete_course,name="delete_course")

]