from django.db import models
# from django.contrib.auth.models import User
# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    student_id = models.CharField(max_length=100,unique=True,null=True, blank=True)
    teacher_id = models.CharField(max_length=100,unique=True,null=True, blank=True)

class auth_profile_customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100,null=True, blank=True)
    phone = models.CharField(blank=True,null=True,max_length=20)
    about = models.TextField(max_length=500, null=True, blank=True)
    image = models.ImageField(blank=True,null=True, upload_to='static/backend/auth_profile/')

class Contact(models.Model):
    name = models.CharField(max_length=300)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=300)
    message = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)