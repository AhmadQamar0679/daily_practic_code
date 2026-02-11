from django.db import models

# Create your models here.

class User(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    Age=models.IntegerField()
    
    def __str__(self):
        return self.first_name
    


class Courses(models.Model):
    course_name=models.CharField(max_length=100)
    Course_image=models.ImageField(upload_to='b_patient/static/media')
    


