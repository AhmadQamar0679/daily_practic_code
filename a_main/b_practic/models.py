from django.db import models

# Create your models here.

class Courses(models.Model):
    course_name=models.CharField(max_length=100)
    course_description=models.TextField()
    course_image=models.ImageField(upload_to='images/')
    
    def __str__(self):
        return self.course_name
    



    
    


