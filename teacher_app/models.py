from auth_dashboard_App.models import User
from django.contrib.auth.models import AbstractUser
from django.db import models

class Teacher_profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True, related_name="Teacher_profile")
    address = models.CharField(max_length=100,null=True, blank=True)
    about = models.TextField(max_length=500, null=True, blank=True)
    department = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(blank=True,null=True,max_length=20)
    image = models.ImageField(blank=True,null=True, upload_to='static/backend/teacher_profile/')
