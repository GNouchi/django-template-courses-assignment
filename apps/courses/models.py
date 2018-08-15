from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length =255)
    create_d = models.DateTimeField(auto_now_add = True)
    update_d = models.DateTimeField(auto_now = True)    

class Description(models.Model):
    text = models.TextField(null = True)
    course = models.OneToOneField(Course, on_delete=models.CASCADE)
    create_d = models.DateTimeField(auto_now_add = True)
    update_d = models.DateTimeField(auto_now = True)